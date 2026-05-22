# Hugging Face Deployment Guide - AI Calculator Agent

## Step-by-Step Deployment Instructions

### 1. Create Hugging Face Account
- Visit: https://huggingface.co/
- Sign up or login

### 2. Create New Space
1. Click on your profile → "New Space"
2. Fill in details:
   - **Space name**: `ai-calculator-agent` (or your choice)
   - **License**: MIT
   - **SDK**: Docker
   - **Space hardware**: CPU basic (free tier)
3. Click "Create Space"

### 3. Upload Files
Upload these files to your Space:
- `app.py`
- `requirements.txt`
- `Dockerfile`
- `README_HF.md` (rename to `README.md`)
- `templates/` folder (with index.html)
- `static/` folder (with style.css and script.js)
- `.gitignore`

### 4. Configure API Key
1. Go to Space Settings → "Variables and secrets"
2. Add new secret:
   - **Name**: `OPENROUTER_API_KEY`
   - **Value**: Your OpenRouter API key from https://openrouter.ai/
3. Save

### 5. Deploy
- Space will automatically build and deploy
- Wait 2-3 minutes for build to complete
- Your app will be live at: `https://huggingface.co/spaces/YOUR_USERNAME/ai-calculator-agent`

## Alternative: Git Push Method

```bash
# Clone your space
git clone https://huggingface.co/spaces/YOUR_USERNAME/ai-calculator-agent
cd ai-calculator-agent

# Copy files
cp -r "E:\nexe_agent_intership\BEGINNER\AI Calculator Agent\*" .

# Rename README
mv README_HF.md README.md

# Commit and push
git add .
git commit -m "Initial deployment"
git push
```

## Troubleshooting

### Build Fails
- Check Dockerfile syntax
- Verify all files are uploaded
- Check Space logs for errors

### App Not Loading
- Verify port 7860 is used in app.py
- Check if API key is set correctly
- Review application logs

### API Errors
- Confirm OpenRouter API key is valid
- Check API key has sufficient credits
- Verify network connectivity

## Testing Your Deployment

Once deployed, test with:
1. "What is 25 + 37?"
2. "Calculate square root of 144"
3. "15 times 8"

## Files Needed for Deployment

✅ app.py (modified for port 7860)
✅ requirements.txt
✅ Dockerfile
✅ README.md (from README_HF.md)
✅ templates/index.html
✅ static/style.css
✅ static/script.js
✅ .gitignore

## Next Steps After Deployment

1. Test all features
2. Share your Space URL
3. Add to your portfolio website
