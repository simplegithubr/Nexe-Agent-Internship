# Getting Started with RAG Assistant

Welcome! This guide will help you set up and run your RAG Assistant in under 10 minutes.

## 📋 What You'll Need

- ✅ Python 3.8 or higher
- ✅ OpenRouter API key (free from https://openrouter.ai/)
- ✅ Web browser (Chrome, Firefox, Edge, Safari)
- ✅ 500MB free disk space

## 🚀 Installation (5 Minutes)

### Step 1: Get Your API Key (2 minutes)

1. Visit **https://openrouter.ai/**
2. Click "Sign Up" (you can use Google/GitHub)
3. Go to "API Keys" section
4. Click "Create Key"
5. Copy your API key (starts with `sk-or-...`)

💡 **Tip**: Keep this key safe! You'll need it in Step 3.

### Step 2: Install Python Dependencies (2 minutes)

Open terminal/command prompt in the project folder:

**Windows:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Mac/Linux:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

⏳ This will take 1-2 minutes to download and install packages.

### Step 3: Configure Your API Key (1 minute)

**Option A: Use Setup Script (Recommended)**

Windows:
```bash
setup_env.bat
```

Mac/Linux:
```bash
bash setup_env.sh
```

**Option B: Manual Setup**

1. Go to `backend` folder
2. Create a file named `.env`
3. Add this line (replace with your actual key):
   ```
   OPENROUTER_API_KEY=sk-or-your-actual-key-here
   ```

## ✅ Verify Installation (1 minute)

Run the verification script:

```bash
cd backend
python verify_setup.py
```

You should see all checks pass:
```
✅ PASS - Python Version
✅ PASS - Dependencies
✅ PASS - Environment Config
✅ PASS - Directories
✅ PASS - Frontend Files
✅ PASS - Sample Document
✅ PASS - Import Tests
```

## 🎯 Running the Application (2 Minutes)

### Start Backend

**Windows:**
```bash
start_backend.bat
```

**Mac/Linux:**
```bash
bash start_backend.sh
```

You should see:
```
Loading embedding model...
Embedding model loaded successfully!
Initializing ChromaDB...
ChromaDB initialized successfully!
Starting RAG Assistant...
 * Running on http://127.0.0.1:5000
```

✅ **Backend is running!** Keep this terminal open.

### Open Frontend

**Option A: Double-click**
- Windows: Double-click `start_frontend.bat`
- Or: Open `frontend/index.html` in your browser

**Option B: Use HTTP Server**
```bash
cd frontend
python -m http.server 8080
```
Then visit: http://localhost:8080

## 🎓 Your First Query (2 Minutes)

### 1. Upload Sample Document

1. In the web interface, click the upload area
2. Select `sample_document.txt` from the project folder
3. Click "Upload Document"
4. Wait for "File uploaded successfully" message

### 2. Ask a Question

Type in the chat:
```
What is Artificial Intelligence?
```

Press Enter or click "Send"

### 3. See the Magic! ✨

You'll get:
- 🤖 AI-generated answer based on your document
- 📄 Source references showing where the answer came from
- 💬 Context snippets from the document

## 🎉 Success!

Congratulations! Your RAG Assistant is working. Try these next:

### More Questions to Try

```
What are the types of AI?
What are the applications of AI in healthcare?
What is machine learning?
What are the challenges in AI?
What is the future of AI?
```

### Upload Your Own Documents

1. Click the upload area
2. Select a PDF, DOCX, or TXT file (max 16MB)
3. Wait for processing
4. Ask questions about your document!

## 🔧 Troubleshooting

### "Module not found" Error

**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

### "API key not configured" Error

**Solution:**
1. Check if `.env` file exists in `backend` folder
2. Open `.env` and verify your API key is correct
3. Make sure there are no extra spaces or quotes
4. Restart the backend

### "Port 5000 already in use" Error

**Solution:**

Windows:
```bash
netstat -ano | findstr :5000
taskkill /PID <PID_NUMBER> /F
```

Mac/Linux:
```bash
lsof -ti:5000 | xargs kill -9
```

### "Cannot connect to backend" Error

**Solution:**
1. Make sure backend is running (check terminal)
2. Look for "Running on http://127.0.0.1:5000" message
3. If you see errors, check your API key in `.env`

### Upload Fails

**Solution:**
- Check file size (must be under 16MB)
- Verify file type (PDF, DOCX, or TXT only)
- Try the sample_document.txt first
- Check backend terminal for error messages

### No Answer or Empty Response

**Solution:**
1. Verify documents are uploaded (check document list)
2. Check your OpenRouter API key is valid
3. Try a simpler question first
4. Check backend terminal for errors

## 📚 Next Steps

### Learn More
- Read `README.md` for detailed documentation
- Check `ARCHITECTURE.md` to understand how it works
- See `DEPLOYMENT.md` to deploy online

### Customize
- Change AI model in `backend/app.py` (line 109)
- Modify chunk size in `backend/app.py` (line 88)
- Customize UI colors in `frontend/index.html`

### Deploy
- Deploy to Hugging Face Spaces (free)
- Host on Render or Railway
- Share with friends!

## 💡 Tips for Best Results

### Document Upload
- ✅ Use clear, well-formatted documents
- ✅ PDFs with selectable text work best
- ✅ Break large documents into smaller files
- ❌ Avoid scanned images (no OCR support yet)

### Asking Questions
- ✅ Be specific: "What are the types of AI?" 
- ✅ Reference document content directly
- ✅ Ask one question at a time
- ❌ Avoid questions outside document scope

### Performance
- First query may be slower (model loading)
- Subsequent queries are faster
- Upload multiple related documents for better context
- Clear database periodically to improve speed

## 🎯 Common Use Cases

### 1. Research Assistant
Upload research papers and ask questions about findings, methodologies, and conclusions.

### 2. Study Helper
Upload textbooks or lecture notes and quiz yourself with questions.

### 3. Document Analysis
Upload contracts, reports, or manuals and extract key information.

### 4. Knowledge Base
Upload company documentation and create a searchable knowledge base.

### 5. Content Summarization
Upload long articles and ask for summaries or specific details.

## 📞 Getting Help

### Check Documentation
1. `README.md` - Complete documentation
2. `TESTING.md` - Testing and debugging
3. `DEPLOYMENT.md` - Deployment guides
4. `ARCHITECTURE.md` - Technical details

### Common Resources
- OpenRouter Status: https://status.openrouter.ai/
- ChromaDB Docs: https://docs.trychroma.com/
- Flask Docs: https://flask.palletsprojects.com/

### Debug Mode
Enable detailed logging:
1. Open `backend/app.py`
2. Find line: `app.run(debug=True, port=5000)`
3. Check terminal for detailed error messages

## ✅ Quick Reference

### Start Backend
```bash
cd backend
python app.py
```

### Test API
```bash
cd backend
python test_api.py
```

### Verify Setup
```bash
cd backend
python verify_setup.py
```

### Clear Database
Use the "Clear All Documents" button in the web interface

### Stop Backend
Press `Ctrl+C` in the terminal

## 🎊 You're All Set!

Your RAG Assistant is ready to help you extract insights from documents. Upload, ask, and discover!

**Happy Querying! 📚🤖**

---

**Need help?** Check TESTING.md for detailed troubleshooting.
**Want to deploy?** See DEPLOYMENT.md for hosting options.
**Curious how it works?** Read ARCHITECTURE.md for technical details.
