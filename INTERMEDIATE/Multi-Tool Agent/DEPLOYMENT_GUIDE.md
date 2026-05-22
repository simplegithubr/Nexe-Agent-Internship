# Hugging Face Deployment Guide - Multi-Tool AI Agent

## Step-by-Step Deployment Instructions

### 1. Create New Space
1. Go to https://huggingface.co/
2. Click on your profile → "New Space"
3. Fill in details:
   - **Space name**: `multi-tool-agent` (or your choice)
   - **License**: MIT
   - **SDK**: Docker
   - **Space hardware**: CPU basic (free tier)
4. Click "Create Space"

### 2. Upload Files
Upload the entire project structure to your Space:

```
Multi-Tool Agent/
├── Dockerfile
├── README.md (rename from README_HF.md)
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── web_search_agent.py
│   │   ├── email_agent.py
│   │   └── openrouter_agent.py
│   └── database/
│       ├── __init__.py
│       └── db.py
└── frontend/
    └── index.html
```

### 3. Configure Secrets (Optional but Recommended)

Go to Space Settings → "Variables and secrets"

#### For Email Features (Optional):
- `SMTP_HOST` = smtp.gmail.com
- `SMTP_PORT` = 587
- `SMTP_USER` = your-email@gmail.com
- `SMTP_PASSWORD` = your-app-password

#### For AI Analysis Features (Optional):
- `OPENROUTER_API_KEY` = your-openrouter-api-key

**Note**: Web search works WITHOUT any API keys! 🎉

### 4. Deploy
- Space will automatically build and deploy
- Wait 3-5 minutes for build to complete (this one is larger)
- Your app will be live at: `https://huggingface.co/spaces/YOUR_USERNAME/multi-tool-agent`

## Alternative: Git Push Method

```bash
# Install git-lfs if not already installed
git lfs install

# Clone your space
git clone https://huggingface.co/spaces/YOUR_USERNAME/multi-tool-agent
cd multi-tool-agent

# Copy entire project
cp -r "E:\nexe_agent_intership\INTERMEDIATE\Multi-Tool Agent\backend" .
cp -r "E:\nexe_agent_intership\INTERMEDIATE\Multi-Tool Agent\frontend" .
cp "E:\nexe_agent_intership\INTERMEDIATE\Multi-Tool Agent\Dockerfile" .
cp "E:\nexe_agent_intership\INTERMEDIATE\Multi-Tool Agent\README_HF.md" README.md

# Commit and push
git add .
git commit -m "Initial deployment of Multi-Tool Agent"
git push
```

## What Works Without Configuration

✅ **Web Search** - DuckDuckGo search (no API key needed)
✅ **News Search** - Latest news articles
✅ **Data Storage** - Save and retrieve data
✅ **Search History** - Track all searches
✅ **Health Check** - Monitor service status

## What Needs Configuration

❌ **Email Sending** - Requires SMTP credentials
❌ **AI Analysis** - Requires OpenRouter API key
❌ **Search Summarization** - Requires OpenRouter API key

## Testing Your Deployment

### Test Web Search (No API key needed)
```bash
curl -X POST https://YOUR_SPACE_URL/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "query": "artificial intelligence",
    "max_results": 5,
    "type": "web"
  }'
```

### Test Data Storage
```bash
# Save data
curl -X POST https://YOUR_SPACE_URL/api/save \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Note",
    "content": "This is a test",
    "category": "test"
  }'

# Retrieve data
curl https://YOUR_SPACE_URL/api/data?category=test
```

### Test Health Check
```bash
curl https://YOUR_SPACE_URL/api/health
```

## Gmail App Password Setup (for Email Feature)

If you want to enable email features:

1. Go to Google Account settings
2. Enable 2-Factor Authentication
3. Go to Security → App Passwords
4. Generate new app password for "Mail"
5. Use this password in `SMTP_PASSWORD` secret

## OpenRouter API Key Setup (for AI Features)

If you want to enable AI analysis:

1. Go to https://openrouter.ai/
2. Sign up / Login
3. Go to Keys section
4. Create new API key
5. Add to Space secrets as `OPENROUTER_API_KEY`

## Troubleshooting

### Build Fails
- Check Dockerfile syntax
- Verify all folders are uploaded correctly
- Check Space logs for Python errors
- Ensure requirements.txt is in backend folder

### Database Errors
- Database is created automatically on first run
- Check if /app/backend/database directory exists
- Review logs for SQLite errors

### Search Not Working
- DuckDuckGo search should work without configuration
- Check network connectivity in logs
- Verify duckduckgo-search package is installed

### Email Not Working
- Verify SMTP credentials are correct
- Check if Gmail allows less secure apps
- Use App Password instead of regular password
- Check Space logs for SMTP errors

### AI Analysis Not Working
- Verify OpenRouter API key is set
- Check if key has sufficient credits
- Review API response in logs

## Files Needed for Deployment

✅ Dockerfile
✅ README.md (from README_HF.md)
✅ backend/app.py (modified for port 7860)
✅ backend/requirements.txt
✅ backend/agents/*.py (all agent files)
✅ backend/database/*.py (database files)
✅ frontend/index.html

## Performance Tips

- Use CPU basic tier for testing
- Upgrade to CPU upgrade for better performance
- Database is persistent across restarts
- Search results are cached in database

## Next Steps After Deployment

1. Test web search functionality
2. Configure optional features (email, AI)
3. Test all API endpoints
4. Share your Space URL
5. Add to your portfolio website

## API Documentation

Once deployed, you can access:
- Web UI: `https://YOUR_SPACE_URL/`
- API Health: `https://YOUR_SPACE_URL/api/health`
- Search History: `https://YOUR_SPACE_URL/api/history/searches`

## Support

If you encounter issues:
1. Check Space logs
2. Verify file structure matches guide
3. Test with curl commands
4. Review error messages in logs
