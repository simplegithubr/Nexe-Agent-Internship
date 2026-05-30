# Deployment Guide for RAG Assistant

## 🚀 Hugging Face Spaces Deployment

### Prerequisites
- Hugging Face account
- OpenRouter API key

### Steps

1. **Create a New Space**
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Name: `rag-assistant`
   - License: MIT
   - SDK: Docker
   - Hardware: CPU Basic (free tier)

2. **Upload Files**
   Upload these files to your Space:
   ```
   - Dockerfile
   - README_HF.md (rename to README.md)
   - backend/ (entire folder)
   - frontend/ (entire folder)
   ```

3. **Set Environment Variables**
   - Go to Space Settings → Variables and secrets
   - Add secret: `OPENROUTER_API_KEY` = your_api_key

4. **Deploy**
   - Space will automatically build and deploy
   - Wait for build to complete (5-10 minutes)
   - Access your app at: `https://huggingface.co/spaces/YOUR_USERNAME/rag-assistant`

### Troubleshooting

**Build fails:**
- Check Dockerfile syntax
- Verify all files are uploaded
- Check build logs in Space

**App doesn't start:**
- Verify OPENROUTER_API_KEY is set
- Check runtime logs
- Ensure port 7860 is exposed

**CORS errors:**
- Frontend should auto-detect API URL
- Check browser console for errors

---

## 🌐 Alternative: Render Deployment

### Backend (Render)

1. Create new Web Service
2. Connect GitHub repository
3. Settings:
   - Build Command: `cd backend && pip install -r requirements.txt`
   - Start Command: `cd backend && python main.py`
   - Environment Variables: Add `OPENROUTER_API_KEY`

### Frontend (Netlify/Vercel)

1. Deploy frontend folder
2. Update API_URL in index.html to your Render backend URL

---

## 💻 Local Development

### Quick Start
```bash
# Windows
start_backend.bat

# Linux/Mac
bash start_backend.sh
```

### Manual Setup
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py

# Frontend
cd frontend
python -m http.server 8080
# Or just open index.html in browser
```

---

## 🔧 Configuration

### Environment Variables
- `OPENROUTER_API_KEY`: Your OpenRouter API key (required)
- `PORT`: Server port (default: 5000 local, 7860 HF Spaces)

### Model Selection
Edit `backend/app.py` line ~109 to change the AI model:
```python
"model": "meta-llama/llama-3.1-8b-instruct:free"
```

Free alternatives:
- `google/gemma-2-9b-it:free`
- `mistralai/mistral-7b-instruct:free`
- `meta-llama/llama-3-8b-instruct:free`

---

## 📊 Monitoring

### Health Check
```bash
curl http://localhost:5000/api/health
```

Response:
```json
{
  "status": "healthy",
  "api_key_set": true,
  "documents_count": 5
}
```

### Logs
- Local: Check terminal output
- HF Spaces: View logs in Space settings
- Render: Check deployment logs

---

## 🔒 Security Notes

1. **Never commit .env file** - It contains your API key
2. **Use environment variables** for sensitive data
3. **Set file size limits** (currently 16MB)
4. **Validate file types** before processing
5. **Clean up uploaded files** after processing

---

## 📈 Scaling

### For Production Use:

1. **Database**: Use persistent storage for ChromaDB
2. **Caching**: Add Redis for query caching
3. **Rate Limiting**: Implement API rate limits
4. **Authentication**: Add user authentication
5. **Monitoring**: Set up error tracking (Sentry)
6. **CDN**: Use CDN for frontend assets

---

## 🐛 Common Issues

### "API key not configured"
- Set OPENROUTER_API_KEY in .env or environment variables

### "Port already in use"
- Change port in app.py or kill process on port 5000

### "Module not found"
- Run `pip install -r requirements.txt`

### "CORS error"
- Ensure backend is running
- Check API_URL in frontend

### "Upload fails"
- Check file size (max 16MB)
- Verify file format (PDF, DOCX, TXT)
- Check backend logs for errors

---

## 📞 Support

For issues or questions:
1. Check logs for error messages
2. Verify API key is set correctly
3. Test with sample_document.txt
4. Check OpenRouter API status

---

**Happy Deploying! 🚀**
