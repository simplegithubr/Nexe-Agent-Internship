# Multi-Tool Agent 🤖

Ek powerful AI agent system jo multiple capabilities provide karta hai:

## Features ✨

- 🔍 **Web Search**: DuckDuckGo se web aur news search
- 💾 **Database Storage**: SQLite database mein data save aur retrieve
- 📧 **Email Sending**: SMTP ke through email bhejein
- 🤖 **AI Analysis**: OpenRouter API use karke intelligent text analysis
- ⚡ **Combined Search & Analysis**: Web search + AI analysis ek saath

## Project Structure 📁

```
Multi-Tool Agent/
├── backend/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── web_search_agent.py      # Web search functionality
│   │   ├── email_agent.py           # Email sending
│   │   └── openrouter_agent.py      # AI analysis
│   ├── database/
│   │   ├── __init__.py
│   │   └── db.py                    # SQLite database operations
│   ├── app.py                       # Flask API server
│   ├── requirements.txt             # Python dependencies
│   └── .env.example                 # Environment variables template
├── frontend/
│   └── index.html                   # Beautiful web UI
└── README.md
```

## Setup Instructions 🚀

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Configure Environment Variables

```bash
# Copy example file
cp .env.example .env

# Edit .env file aur apni API keys add karein
```

**Required Configuration:**

```env
# OpenRouter API Key (Required for AI features)
OPENROUTER_API_KEY=your_key_here

# Email Configuration (Optional)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

### 3. Run the Application

```bash
cd backend
python app.py
```

Server start ho jayega: `http://localhost:5000`

### 4. Open Browser

Browser mein jao: `http://localhost:5000`

## API Endpoints 🔌

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/health` | GET | Health check |
| `/api/search` | POST | Web/news search |
| `/api/save` | POST | Save data to DB |
| `/api/data` | GET | Retrieve saved data |
| `/api/email` | POST | Send email |
| `/api/analyze` | POST | AI text analysis |
| `/api/search-and-analyze` | POST | Combined search + AI |

## Getting API Keys 🔑

### OpenRouter API Key

1. Visit: https://openrouter.ai/
2. Sign up/login
3. Go to "Keys" section
4. Create new API key
5. Copy aur `.env` file mein paste karein

### Gmail SMTP (for Email)

1. Gmail account mein 2-factor authentication enable karein
2. App Password generate karein
3. `.env` file mein add karein

## Usage Examples 💡

### Web Search
```json
POST /api/search
{
  "query": "Python programming",
  "type": "web",
  "max_results": 5
}
```

### Save Data
```json
POST /api/save
{
  "title": "My Note",
  "content": "Important information",
  "category": "notes"
}
```

### AI Analysis
```json
POST /api/analyze
{
  "prompt": "Explain quantum computing",
  "model": "anthropic/claude-3.5-sonnet"
}
```

## Technologies Used 🛠️

- **Backend**: Flask, Python
- **Database**: SQLite
- **Search**: DuckDuckGo API
- **AI**: OpenRouter API
- **Frontend**: HTML, CSS, JavaScript
- **Email**: SMTP

## Features in Detail 📝

### 1. Web Search Agent
- DuckDuckGo integration
- Web aur news search
- Results database mein save hote hain

### 2. Database Agent
- SQLite database
- Search history
- Saved data with categories
- Email logs
- AI analysis history

### 3. Email Agent
- SMTP support
- Plain text aur HTML emails
- Email sending logs

### 4. OpenRouter Agent
- Multiple AI models support
- Claude, GPT-4, Gemini, Llama
- Token usage tracking
- Search results summarization

## Troubleshooting 🔧

**Problem**: OpenRouter agent not initialized
- **Solution**: `.env` file mein `OPENROUTER_API_KEY` add karein

**Problem**: Email not sending
- **Solution**: SMTP credentials check karein, Gmail App Password use karein

**Problem**: Port 5000 already in use
- **Solution**: `app.py` mein port number change karein

## Future Enhancements 🚀

- [ ] User authentication
- [ ] File upload support
- [ ] More AI models
- [ ] Export data to CSV/JSON
- [ ] Scheduled tasks
- [ ] API rate limiting

## License 📄

MIT License - Free to use and modify

## Support 💬

Issues ya questions ke liye GitHub issues use karein.

---

**Made with ❤️ using Claude Code**
