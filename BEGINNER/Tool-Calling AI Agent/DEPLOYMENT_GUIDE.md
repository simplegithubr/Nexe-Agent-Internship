# Hugging Face Deployment Guide - Tool-Calling AI Agent

## Step-by-Step Deployment Instructions

### 1. Create New Space
1. Go to https://huggingface.co/
2. Click on your profile → "New Space"
3. Fill in details:
   - **Space name**: `tool-calling-agent` (or your choice)
   - **License**: MIT
   - **SDK**: Docker
   - **Space hardware**: CPU basic (free tier)
4. Click "Create Space"

### 2. Upload Files
Upload these files to your Space:
- `app.py` (modified for port 7860)
- `agent.py`
- `requirements.txt`
- `Dockerfile`
- `README_HF.md` (rename to `README.md`)
- `templates/` folder (with index.html)
- `static/` folder (with style.css and script.js)
- `.gitignore`

### 3. Deploy
- Space will automatically build and deploy
- Wait 2-3 minutes for build to complete
- Your app will be live at: `https://huggingface.co/spaces/YOUR_USERNAME/tool-calling-agent`

## Alternative: Git Push Method

```bash
# Clone your space
git clone https://huggingface.co/spaces/YOUR_USERNAME/tool-calling-agent
cd tool-calling-agent

# Copy files
cp -r "E:\nexe_agent_intership\BEGINNER\Tool-Calling AI Agent\*" .

# Rename README
mv README_HF.md README.md

# Commit and push
git add .
git commit -m "Initial deployment"
git push
```

## No API Keys Required! 🎉

This agent doesn't need any external API keys. It uses pure Python implementations of all tools.

## Testing Your Deployment

Once deployed, test with:

### Calculator
```json
{
  "tool": "calculator",
  "params": {
    "operation": "add",
    "num1": 15,
    "num2": 25
  }
}
```

### Weather
```json
{
  "tool": "weather",
  "params": {
    "city": "London"
  }
}
```

### Text Analyzer
```json
{
  "tool": "text_analyzer",
  "params": {
    "text": "Hello world! This is a test."
  }
}
```

## Files Needed for Deployment

✅ app.py (modified for port 7860)
✅ agent.py
✅ requirements.txt
✅ Dockerfile
✅ README.md (from README_HF.md)
✅ templates/index.html
✅ static/style.css
✅ static/script.js
✅ .gitignore

## Troubleshooting

### Build Fails
- Check Dockerfile syntax
- Verify all files are uploaded
- Check Space logs for errors

### App Not Loading
- Verify port 7860 is used in app.py
- Check application logs in Space

### Tool Not Working
- Check JSON format in request
- Verify tool name is correct
- Review application logs

## Next Steps After Deployment

1. Test all four tools
2. Share your Space URL
3. Add to your portfolio website
4. Customize tools or add new ones
