# RAG Assistant - Testing Guide

## 🧪 Testing Your Installation

### 1. Setup Verification

Before running the app, verify your setup:

```bash
cd backend
python verify_setup.py
```

This will check:
- ✅ Python version (3.8+)
- ✅ All dependencies installed
- ✅ Environment variables configured
- ✅ Required directories exist
- ✅ Frontend files present
- ✅ Critical imports working

### 2. API Testing

After starting the backend, test all endpoints:

```bash
cd backend
python test_api.py
```

This will test:
- ✅ Backend health check
- ✅ Document upload
- ✅ Document listing
- ✅ Query/answer system
- ✅ Database clearing

## 📝 Manual Testing Steps

### Step 1: Start Backend

```bash
cd backend
python app.py
```

Expected output:
```
Loading embedding model...
Embedding model loaded successfully!
Initializing ChromaDB...
ChromaDB initialized successfully!
Starting RAG Assistant...
API Key configured: True
 * Running on http://127.0.0.1:5000
```

### Step 2: Test Health Endpoint

```bash
curl http://localhost:5000/api/health
```

Expected response:
```json
{
  "status": "healthy",
  "api_key_set": true,
  "documents_count": 0
}
```

### Step 3: Upload Sample Document

Using curl:
```bash
curl -X POST -F "file=@../sample_document.txt" http://localhost:5000/api/upload
```

Expected response:
```json
{
  "message": "File uploaded and processed successfully",
  "filename": "sample_document.txt",
  "chunks": 15
}
```

### Step 4: Query the System

```bash
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is Artificial Intelligence?"}'
```

Expected response:
```json
{
  "answer": "Artificial Intelligence (AI) refers to...",
  "context": [
    {
      "text": "Artificial Intelligence (AI) refers to...",
      "source": "sample_document.txt"
    }
  ]
}
```

### Step 5: List Documents

```bash
curl http://localhost:5000/api/documents
```

Expected response:
```json
{
  "documents": ["sample_document.txt"],
  "total_chunks": 15
}
```

### Step 6: Test Frontend

1. Open `frontend/index.html` in your browser
2. Upload a document
3. Ask questions in the chat
4. Verify answers appear with context

## 🎯 Test Cases

### Test Case 1: PDF Upload
1. Upload a PDF file
2. Verify chunks are created
3. Ask questions about PDF content
4. Verify accurate answers

### Test Case 2: Multiple Documents
1. Upload 3 different documents
2. Verify all appear in document list
3. Ask questions spanning multiple documents
4. Verify context from correct sources

### Test Case 3: Large Document
1. Upload a document > 5 pages
2. Verify chunking works correctly
3. Ask specific questions
4. Verify relevant chunks are retrieved

### Test Case 4: Error Handling
1. Try uploading invalid file type
2. Try uploading file > 16MB
3. Ask question with no documents
4. Verify appropriate error messages

### Test Case 5: Clear Database
1. Upload documents
2. Clear database
3. Verify documents are removed
4. Verify queries return "no documents" message

## 🐛 Common Issues & Solutions

### Issue: "Module not found"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "API key not configured"
**Solution:**
1. Create `.env` file in backend folder
2. Add: `OPENROUTER_API_KEY=your_actual_key`

### Issue: "Port 5000 already in use"
**Solution:**
```bash
# Find and kill process on port 5000
# Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac:
lsof -ti:5000 | xargs kill -9
```

### Issue: "CORS error"
**Solution:**
- Ensure backend is running
- Check API_URL in frontend matches backend URL
- Verify flask-cors is installed

### Issue: "Empty answer"
**Solution:**
- Check OpenRouter API key is valid
- Verify documents are uploaded
- Check backend logs for errors
- Test with sample_document.txt first

### Issue: "Upload fails"
**Solution:**
- Check file size (max 16MB)
- Verify file format (PDF, DOCX, TXT)
- Check backend logs for specific error
- Ensure uploads directory has write permissions

## 📊 Performance Testing

### Test Response Times

```python
import time
import requests

# Test query speed
start = time.time()
response = requests.post(
    "http://localhost:5000/api/query",
    json={"question": "What is AI?"}
)
end = time.time()

print(f"Query time: {end - start:.2f} seconds")
```

Expected times:
- Health check: < 0.1s
- Document upload: 2-10s (depends on size)
- Query: 2-5s (includes AI generation)
- List documents: < 0.1s

## ✅ Acceptance Criteria

Your RAG Assistant is working correctly if:

1. ✅ Backend starts without errors
2. ✅ Health endpoint returns healthy status
3. ✅ Documents upload successfully
4. ✅ Chunks are created and stored
5. ✅ Queries return relevant answers
6. ✅ Context sources are displayed
7. ✅ Frontend UI is responsive
8. ✅ Multiple documents can be uploaded
9. ✅ Database can be cleared
10. ✅ Error messages are clear and helpful

## 🔄 Continuous Testing

Run tests after:
- Installing new dependencies
- Changing API endpoints
- Modifying document processing
- Updating AI prompts
- Deploying to production

## 📝 Test Checklist

Before deployment:
- [ ] All automated tests pass
- [ ] Manual testing completed
- [ ] Error handling verified
- [ ] Performance acceptable
- [ ] Frontend responsive on mobile
- [ ] API key secured
- [ ] Logs are clean
- [ ] Documentation updated

---

**Happy Testing! 🧪**
