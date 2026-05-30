# Frequently Asked Questions (FAQ)

## 🤔 General Questions

### What is RAG Assistant?
RAG Assistant is a Retrieval-Augmented Generation system that lets you upload documents and ask questions to get AI-powered contextual answers. It combines semantic search with large language models to provide accurate, source-backed responses.

### Is it free to use?
Yes! The project is open source (MIT License) and uses OpenRouter's free tier for AI models. You only need a free OpenRouter account.

### What file types are supported?
Currently supports:
- PDF (.pdf)
- Microsoft Word (.docx)
- Plain text (.txt)

Maximum file size: 16MB

### How does it work?
1. You upload documents
2. Text is extracted and split into chunks
3. Chunks are converted to embeddings (numerical representations)
4. Embeddings are stored in a vector database
5. When you ask a question, relevant chunks are retrieved
6. AI generates an answer based on those chunks

---

## 🔧 Setup & Installation

### What are the system requirements?
- Python 3.8 or higher
- 500MB free disk space
- Internet connection
- Modern web browser

### Do I need to install anything?
Yes, you need to:
1. Install Python dependencies: `pip install -r requirements.txt`
2. Get a free OpenRouter API key
3. Create a `.env` file with your API key

### How do I get an OpenRouter API key?
1. Visit https://openrouter.ai/
2. Sign up (free, can use Google/GitHub)
3. Go to API Keys section
4. Create a new key
5. Copy and save it

### Where do I put my API key?
Create a file named `.env` in the `backend` folder with:
```
OPENROUTER_API_KEY=your_actual_key_here
```

Or use the setup script: `setup_env.bat` (Windows) or `bash setup_env.sh` (Mac/Linux)

### Installation fails with "Module not found"
Run: `pip install -r requirements.txt` from the backend folder

Make sure you're in the virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

---

## 🚀 Usage

### How do I start the application?
1. Start backend: `python app.py` (from backend folder)
2. Open frontend: Open `frontend/index.html` in browser

Or use the helper scripts:
- Windows: `start_backend.bat`
- Mac/Linux: `bash start_backend.sh`

### Can I upload multiple documents?
Yes! Upload as many documents as you want. The system will search across all of them when answering questions.

### What's the maximum file size?
16MB per file. For larger documents, consider splitting them into smaller files.

### How long does upload take?
Typically 2-10 seconds depending on:
- File size
- Number of pages
- Text complexity
- Your computer speed

### Why is my first query slow?
The first query loads the AI model, which takes a few seconds. Subsequent queries are much faster (3-5 seconds).

### Can I ask questions in other languages?
The AI model supports multiple languages, but works best with English. You can try asking in other languages, but accuracy may vary.

### How accurate are the answers?
Answers are based on your uploaded documents. Accuracy depends on:
- Quality of your documents
- Clarity of your question
- Relevance of document content
- AI model capabilities

Always verify important information from the source documents.

---

## 🔍 Troubleshooting

### "Cannot connect to backend" error
**Causes:**
- Backend not running
- Wrong port
- Firewall blocking

**Solutions:**
1. Check if backend is running (look for "Running on http://127.0.0.1:5000")
2. Restart backend: `python app.py`
3. Check firewall settings

### "API key not configured" error
**Solutions:**
1. Create `.env` file in backend folder
2. Add: `OPENROUTER_API_KEY=your_key`
3. Restart backend
4. Verify no extra spaces or quotes

### "Port 5000 already in use" error
**Solutions:**

Windows:
```bash
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

Mac/Linux:
```bash
lsof -ti:5000 | xargs kill -9
```

Or change port in `app.py`: `app.run(debug=True, port=5001)`

### Upload fails
**Common causes:**
- File too large (>16MB)
- Unsupported file type
- Corrupted file
- No write permissions

**Solutions:**
1. Check file size and type
2. Try sample_document.txt first
3. Check backend logs for specific error
4. Ensure uploads folder has write permissions

### No answer or empty response
**Solutions:**
1. Verify documents are uploaded (check document list)
2. Check API key is valid
3. Try a simpler question
4. Check backend terminal for errors
5. Verify internet connection

### CORS errors in browser
**Solutions:**
1. Ensure backend is running
2. Check API_URL in frontend matches backend
3. Verify flask-cors is installed: `pip install flask-cors`

### PDF upload fails but TXT works
**Cause:** PDF might be scanned image (no text layer)

**Solutions:**
1. Use PDFs with selectable text
2. Convert scanned PDFs with OCR first
3. Try extracting text manually and upload as TXT

### Answers are not relevant
**Possible reasons:**
- Question not related to documents
- Documents don't contain the information
- Question too vague

**Solutions:**
1. Upload more relevant documents
2. Ask more specific questions
3. Check if documents actually contain the information

---

## 💻 Technical Questions

### What AI model is used?
LLaMA 3.1 8B Instruct (free tier on OpenRouter)

You can change it in `backend/app.py` line 109. Other free options:
- `google/gemma-2-9b-it:free`
- `mistralai/mistral-7b-instruct:free`

### What is the embedding model?
Sentence Transformers: `all-MiniLM-L6-v2`

This creates 384-dimensional embeddings for semantic search.

### What database is used?
ChromaDB - an open-source vector database optimized for embeddings.

### How is text chunked?
- Chunk size: 500 characters
- Overlap: 50 characters
- Method: Recursive character splitting (LangChain)

### Can I change chunk size?
Yes, edit `backend/app.py` around line 88:
```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,  # Change this
    chunk_overlap=50,  # And this
    length_function=len,
)
```

### Where is data stored?
- Vector embeddings: `backend/chroma_db/` (persistent)
- Uploaded files: `backend/uploads/` (temporary, deleted after processing)

### Is my data secure?
- Documents processed locally
- Only question + context sent to OpenRouter
- API key stored in `.env` (not committed to git)
- No data stored on external servers (except OpenRouter API calls)

### Can I use a different AI provider?
Yes, but you'll need to modify `backend/app.py` to use a different API. The code is structured to make this relatively easy.

### Can I run this offline?
Partially. You can:
- Process documents offline
- Search documents offline
- But need internet for AI answer generation (OpenRouter API)

For fully offline, you'd need to run a local LLM (like Ollama).

---

## 🌐 Deployment

### Can I deploy this online?
Yes! See DEPLOYMENT.md for detailed instructions.

Recommended platforms:
- Hugging Face Spaces (free, Docker-based)
- Render (free tier available)
- Railway (free tier available)

### How do I deploy to Hugging Face Spaces?
1. Create a Space (Docker SDK)
2. Upload all files
3. Add OPENROUTER_API_KEY as a secret
4. Wait for build to complete

See DEPLOYMENT.md for step-by-step guide.

### Can multiple users use it simultaneously?
The current version is single-threaded. For production with multiple users:
1. Use Gunicorn/uWSGI for multi-threading
2. Add user authentication
3. Separate vector stores per user
4. Use a production database

### What about scaling?
For high traffic:
- Use load balancer
- Separate ChromaDB instance
- Cache frequent queries
- Use CDN for frontend
- Implement rate limiting

---

## 📊 Performance

### How fast is it?
- Document upload: 2-10 seconds
- Query processing: 3-8 seconds
- Search: <1 second
- First query: Slower (model loading)

### Can I make it faster?
Yes:
1. Use smaller chunk sizes
2. Reduce number of retrieved chunks
3. Use faster embedding model
4. Cache frequent queries
5. Use SSD for ChromaDB storage

### How many documents can I upload?
No hard limit, but performance degrades with:
- 100+ documents: Slower search
- 1000+ documents: Consider optimization
- 10,000+ documents: Need production setup

### How much RAM does it need?
- Minimum: 2GB
- Recommended: 4GB+
- With large documents: 8GB+

---

## 🔐 Security & Privacy

### Is my data private?
- Documents processed locally
- Only question + context sent to OpenRouter
- No data stored on external servers (except API calls)

### What does OpenRouter see?
Only:
- Your question
- Relevant document chunks (context)
- Not your full documents

### Should I upload sensitive documents?
Use caution with:
- Personal information
- Confidential business data
- Medical records
- Financial information

Consider:
- Running locally only
- Using a local LLM instead of OpenRouter
- Redacting sensitive information first

### Can I use this for HIPAA/GDPR compliance?
Not out of the box. You'd need:
- Local LLM (no external API)
- Encryption at rest
- Access controls
- Audit logging
- Data retention policies

---

## 🎯 Best Practices

### What makes a good document?
- Clear, well-formatted text
- Proper headings and structure
- Selectable text (not scanned images)
- Relevant to your questions
- Not too long (split large docs)

### How should I ask questions?
✅ Good:
- "What are the three types of AI mentioned?"
- "According to the document, what is machine learning?"
- "List the applications of AI in healthcare"

❌ Avoid:
- "Tell me everything"
- Questions outside document scope
- Multiple questions at once

### How many documents should I upload?
- Start with 1-3 related documents
- Add more as needed
- Group by topic
- Clear database between different topics

### When should I clear the database?
- Switching to a different topic
- Database getting too large
- Answers becoming less relevant
- Starting a new project

---

## 🆘 Still Need Help?

### Documentation
- README.md - Complete documentation
- GETTING_STARTED.md - Setup guide
- TESTING.md - Troubleshooting
- ARCHITECTURE.md - Technical details

### Check Logs
Backend terminal shows detailed error messages when debug=True

### Test with Sample
Always test with `sample_document.txt` first to verify setup

### Common Resources
- OpenRouter: https://openrouter.ai/
- ChromaDB: https://docs.trychroma.com/
- Flask: https://flask.palletsprojects.com/

---

**Still stuck? Check TESTING.md for detailed troubleshooting steps!**
