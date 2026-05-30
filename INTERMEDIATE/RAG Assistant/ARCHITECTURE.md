# RAG Assistant - Project Architecture

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  HTML/CSS/JavaScript (Vanilla)                       │  │
│  │  - Document Upload UI                                │  │
│  │  - Chat Interface                                    │  │
│  │  - Document Management                               │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                            │ HTTP/REST API
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      Flask Backend                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  API Endpoints                                       │  │
│  │  - /api/upload    - /api/query                      │  │
│  │  - /api/documents - /api/clear                      │  │
│  │  - /api/health                                      │  │
│  └──────────────────────────────────────────────────────┘  │
│                            │                                 │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Document Processing Pipeline                        │  │
│  │  1. Extract text (PDF/DOCX/TXT)                     │  │
│  │  2. Split into chunks (500 chars)                   │  │
│  │  3. Generate embeddings                             │  │
│  │  4. Store in vector database                        │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
┌──────────────────────────┐  ┌──────────────────────────┐
│   Vector Store           │  │   AI Model               │
│   (ChromaDB)             │  │   (OpenRouter)           │
│                          │  │                          │
│  - Embeddings storage    │  │  - LLaMA 3.1 8B         │
│  - Semantic search       │  │  - Answer generation     │
│  - Cosine similarity     │  │  - Context-aware         │
└──────────────────────────┘  └──────────────────────────┘
```

## 📊 Data Flow

### Upload Flow
```
1. User uploads document (PDF/DOCX/TXT)
   ↓
2. Backend extracts text content
   ↓
3. Text split into chunks (500 chars, 50 overlap)
   ↓
4. Sentence Transformer generates embeddings
   ↓
5. Embeddings + chunks stored in ChromaDB
   ↓
6. Success response with chunk count
```

### Query Flow
```
1. User asks question
   ↓
2. Question converted to embedding
   ↓
3. ChromaDB searches for similar chunks (top 3)
   ↓
4. Relevant chunks retrieved with metadata
   ↓
5. Context + question sent to OpenRouter
   ↓
6. LLaMA 3.1 generates contextual answer
   ↓
7. Answer + sources returned to user
```

## 🔧 Technology Stack

### Backend
- **Flask**: Web framework for REST API
- **ChromaDB**: Vector database for embeddings
- **Sentence Transformers**: Text embedding model (all-MiniLM-L6-v2)
- **LangChain**: Text splitting and processing
- **PyPDF2**: PDF text extraction
- **python-docx**: DOCX text extraction
- **OpenRouter API**: Access to LLaMA 3.1 8B (free tier)

### Frontend
- **Vanilla JavaScript**: No framework dependencies
- **Modern CSS**: Gradients, animations, responsive design
- **Fetch API**: HTTP requests to backend

### Storage
- **ChromaDB**: Persistent vector storage
- **File System**: Temporary document uploads

## 📁 Project Structure

```
RAG Assistant/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── main.py                # Entry point for deployment
│   ├── requirements.txt       # Python dependencies
│   ├── verify_setup.py        # Setup verification script
│   ├── test_api.py           # API testing suite
│   ├── .env                  # Environment variables (create this)
│   ├── uploads/              # Temporary file storage (auto-created)
│   └── chroma_db/            # Vector database (auto-created)
│
├── frontend/
│   └── index.html            # Complete web interface
│
├── docs/
│   ├── README.md             # Main documentation
│   ├── QUICKSTART.txt        # Quick start guide
│   ├── DEPLOYMENT.md         # Deployment instructions
│   ├── TESTING.md            # Testing guide
│   └── ARCHITECTURE.md       # This file
│
├── scripts/
│   ├── start_backend.bat     # Windows backend launcher
│   ├── start_backend.sh      # Linux/Mac backend launcher
│   ├── start_frontend.bat    # Windows frontend launcher
│   ├── setup_env.bat         # Windows env setup
│   └── setup_env.sh          # Linux/Mac env setup
│
├── config/
│   ├── .env.example          # Environment template
│   ├── .gitignore           # Git ignore rules
│   └── Dockerfile           # Docker configuration
│
├── samples/
│   └── sample_document.txt   # Test document
│
├── package.json              # Project metadata
├── LICENSE                   # MIT License
└── README_HF.md             # Hugging Face Spaces README
```

## 🔐 Security Considerations

### API Key Management
- API keys stored in `.env` file (not committed)
- Environment variables used in production
- Keys never exposed in frontend code

### File Upload Security
- File type validation (PDF, DOCX, TXT only)
- File size limit (16MB max)
- Secure filename handling
- Temporary storage with cleanup

### CORS Configuration
- CORS enabled for local development
- Configure allowed origins for production

## 🚀 Deployment Options

### 1. Local Development
- Direct Python execution
- Simple HTTP server for frontend
- Best for: Testing and development

### 2. Hugging Face Spaces
- Docker-based deployment
- Free tier available
- Best for: Public demos

### 3. Cloud Platforms
- Render, Railway, Fly.io
- Separate frontend/backend
- Best for: Production use

## 📈 Scalability Considerations

### Current Limitations
- Single-threaded Flask server
- In-memory embedding model
- Local file storage
- No authentication

### Production Improvements
1. **Backend**: Use Gunicorn/uWSGI for multi-threading
2. **Database**: Separate ChromaDB instance
3. **Storage**: S3/Cloud storage for documents
4. **Caching**: Redis for query caching
5. **Auth**: JWT-based authentication
6. **Monitoring**: Logging and error tracking
7. **Rate Limiting**: API rate limits per user

## 🔄 Future Enhancements

### Planned Features
- [ ] Multi-user support with authentication
- [ ] Document versioning
- [ ] Advanced search filters
- [ ] Export chat history
- [ ] Support for more file types (CSV, JSON, XML)
- [ ] Batch document upload
- [ ] Custom embedding models
- [ ] Multiple AI model options
- [ ] Conversation memory
- [ ] Document summarization

### Technical Improvements
- [ ] WebSocket for real-time updates
- [ ] Progressive web app (PWA)
- [ ] Mobile app (React Native)
- [ ] GraphQL API
- [ ] Microservices architecture
- [ ] Kubernetes deployment
- [ ] CI/CD pipeline
- [ ] Automated testing

## 📊 Performance Metrics

### Expected Performance
- **Document Upload**: 2-10 seconds (depends on size)
- **Embedding Generation**: 1-3 seconds per chunk
- **Query Search**: < 1 second
- **AI Answer Generation**: 2-5 seconds
- **Total Query Time**: 3-8 seconds

### Optimization Opportunities
1. Cache frequently asked questions
2. Batch embedding generation
3. Async document processing
4. CDN for frontend assets
5. Database query optimization

## 🧪 Testing Strategy

### Unit Tests
- Document processing functions
- Embedding generation
- Vector search accuracy

### Integration Tests
- API endpoint testing
- End-to-end upload flow
- Query and answer flow

### Performance Tests
- Load testing with multiple users
- Large document handling
- Concurrent query processing

## 📝 API Documentation

### Endpoints

#### GET /api/health
Health check endpoint
```json
Response: {
  "status": "healthy",
  "api_key_set": true,
  "documents_count": 5
}
```

#### POST /api/upload
Upload and process document
```
Request: multipart/form-data with 'file' field
Response: {
  "message": "File uploaded and processed successfully",
  "filename": "document.pdf",
  "chunks": 25
}
```

#### POST /api/query
Ask question about documents
```json
Request: {
  "question": "What is AI?"
}
Response: {
  "answer": "AI is...",
  "context": [
    {"text": "...", "source": "document.pdf"}
  ]
}
```

#### GET /api/documents
List uploaded documents
```json
Response: {
  "documents": ["doc1.pdf", "doc2.txt"],
  "total_chunks": 50
}
```

#### POST /api/clear
Clear all documents
```json
Response: {
  "message": "Database cleared successfully"
}
```

---

**Architecture designed for simplicity, scalability, and maintainability.**
