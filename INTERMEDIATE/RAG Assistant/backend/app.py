from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import PyPDF2
import docx
from langchain.text_splitter import RecursiveCharacterTextSplitter
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Initialize embedding model
print("Loading embedding model...")
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
print("Embedding model loaded successfully!")

# Initialize ChromaDB
print("Initializing ChromaDB...")
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection(
    name="documents",
    metadata={"hnsw:space": "cosine"}
)
print("ChromaDB initialized successfully!")

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', '')
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

if not OPENROUTER_API_KEY:
    print("WARNING: OPENROUTER_API_KEY not set in environment variables!")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except Exception as e:
        print(f"Error extracting PDF: {e}")
        raise
    return text

def extract_text_from_docx(file_path):
    try:
        doc = docx.Document(file_path)
        return '\n'.join([paragraph.text for paragraph in doc.paragraphs if paragraph.text.strip()])
    except Exception as e:
        print(f"Error extracting DOCX: {e}")
        raise

def extract_text_from_txt(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except UnicodeDecodeError:
        # Try with different encoding
        with open(file_path, 'r', encoding='latin-1') as file:
            return file.read()

def process_document(file_path, filename):
    ext = filename.rsplit('.', 1)[1].lower()

    print(f"Processing {filename} ({ext})...")

    if ext == 'pdf':
        text = extract_text_from_pdf(file_path)
    elif ext == 'docx':
        text = extract_text_from_docx(file_path)
    elif ext == 'txt':
        text = extract_text_from_txt(file_path)
    else:
        return None

    if not text or len(text.strip()) < 10:
        raise ValueError("Document appears to be empty or too short")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )
    chunks = text_splitter.split_text(text)

    print(f"Created {len(chunks)} chunks from {filename}")
    return chunks

def add_to_vector_store(chunks, filename):
    print(f"Generating embeddings for {len(chunks)} chunks...")
    embeddings = embedding_model.encode(chunks).tolist()

    ids = [f"{filename}_{i}_{datetime.now().timestamp()}" for i in range(len(chunks))]
    metadatas = [{"source": filename, "chunk_id": i} for i in range(len(chunks))]

    collection.add(
        embeddings=embeddings,
        documents=chunks,
        metadatas=metadatas,
        ids=ids
    )

    print(f"Added {len(chunks)} chunks to vector store")
    return len(chunks)

def retrieve_relevant_chunks(query, n_results=3):
    print(f"Searching for: {query}")
    query_embedding = embedding_model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    if results['documents']:
        print(f"Found {len(results['documents'][0])} relevant chunks")
        return results['documents'][0], results['metadatas'][0]
    return [], []

def generate_answer(query, context_chunks):
    if not OPENROUTER_API_KEY:
        return "Error: OpenRouter API key not configured. Please set OPENROUTER_API_KEY in environment variables."

    context = "\n\n".join([f"[{i+1}] {chunk}" for i, chunk in enumerate(context_chunks)])

    prompt = f"""You are a helpful assistant. Answer the user's question based on the provided context.

Context:
{context}

Question: {query}

Answer the question based on the context above. If the answer is not in the context, say "I don't have enough information to answer this question based on the uploaded documents." Be concise and accurate."""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://huggingface.co/spaces",
        "X-Title": "RAG Assistant"
    }

    data = {
        "model": "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 500
    }

    try:
        print("Calling OpenRouter API...")
        response = requests.post(OPENROUTER_URL, headers=headers, json=data, timeout=30)
        response.raise_for_status()
        result = response.json()
        answer = result['choices'][0]['message']['content']
        print("Answer generated successfully")
        return answer
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return f"Error generating answer: {str(e)}"
    except Exception as e:
        print(f"Unexpected error: {e}")
        return f"Error: {str(e)}"

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        try:
            file.save(filepath)
            print(f"File saved: {filepath}")

            chunks = process_document(filepath, filename)
            if chunks:
                num_chunks = add_to_vector_store(chunks, filename)
                return jsonify({
                    'message': 'File uploaded and processed successfully',
                    'filename': filename,
                    'chunks': num_chunks
                }), 200
            else:
                return jsonify({'error': 'Failed to process document'}), 500
        except Exception as e:
            print(f"Error processing file: {e}")
            return jsonify({'error': f'Error processing file: {str(e)}'}), 500
        finally:
            # Clean up uploaded file
            if os.path.exists(filepath):
                try:
                    os.remove(filepath)
                except:
                    pass

    return jsonify({'error': 'Invalid file type. Allowed: PDF, DOCX, TXT'}), 400

@app.route('/api/query', methods=['POST'])
def query():
    data = request.json
    question = data.get('question', '')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    try:
        chunks, metadatas = retrieve_relevant_chunks(question, n_results=3)

        if not chunks:
            return jsonify({
                'answer': 'No documents have been uploaded yet. Please upload documents first.',
                'context': []
            }), 200

        answer = generate_answer(question, chunks)

        return jsonify({
            'answer': answer,
            'context': [
                {'text': chunk[:200] + '...' if len(chunk) > 200 else chunk, 'source': meta['source']}
                for chunk, meta in zip(chunks, metadatas)
            ]
        }), 200
    except Exception as e:
        print(f"Query error: {e}")
        return jsonify({'error': f'Error processing query: {str(e)}'}), 500

@app.route('/api/documents', methods=['GET'])
def get_documents():
    try:
        all_docs = collection.get()
        sources = set()
        if all_docs['metadatas']:
            sources = set([meta['source'] for meta in all_docs['metadatas']])

        return jsonify({
            'documents': sorted(list(sources)),
            'total_chunks': len(all_docs['ids']) if all_docs['ids'] else 0
        }), 200
    except Exception as e:
        print(f"Error fetching documents: {e}")
        return jsonify({'error': f'Error fetching documents: {str(e)}'}), 500

@app.route('/api/clear', methods=['POST'])
def clear_database():
    try:
        print("Clearing database...")
        chroma_client.delete_collection("documents")
        global collection
        collection = chroma_client.get_or_create_collection(
            name="documents",
            metadata={"hnsw:space": "cosine"}
        )
        print("Database cleared successfully")
        return jsonify({'message': 'Database cleared successfully'}), 200
    except Exception as e:
        print(f"Error clearing database: {e}")
        return jsonify({'error': f'Error clearing database: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'api_key_set': bool(OPENROUTER_API_KEY),
        'documents_count': len(collection.get()['ids']) if collection.get()['ids'] else 0
    }), 200

if __name__ == '__main__':
    print("Starting RAG Assistant...")
    print(f"API Key configured: {bool(OPENROUTER_API_KEY)}")
    app.run(debug=True, port=5000)
