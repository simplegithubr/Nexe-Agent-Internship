---
title: Multi-Tool AI Agent
emoji: 🤖
colorFrom: purple
colorTo: pink
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# Multi-Tool AI Agent 🤖

An advanced AI agent system with multiple integrated tools for web search, email, data storage, and AI-powered analysis.

## Features

### 🔍 Web Search Agent
- Search the web using DuckDuckGo
- Search news articles
- Get real-time search results
- No API key required for search

### 📧 Email Agent
- Send emails programmatically
- Support for HTML emails
- Email logging and history
- Requires SMTP configuration

### 💾 Data Storage
- SQLite database for persistent storage
- Save and retrieve data with categories
- Search history tracking
- Analysis history

### 🤖 AI Analysis (Optional)
- Powered by OpenRouter API
- Multiple AI models support
- Search result summarization
- Custom prompt analysis
- Requires OpenRouter API key

## API Endpoints

### Search
- `POST /api/search` - Web search
  ```json
  {
    "query": "your search query",
    "max_results": 5,
    "type": "web"  // or "news"
  }
  ```

### Data Storage
- `POST /api/save` - Save data
- `GET /api/data` - Retrieve data

### Email
- `POST /api/email` - Send email
  ```json
  {
    "recipient": "email@example.com",
    "subject": "Subject",
    "body": "Email body",
    "html": false
  }
  ```

### AI Analysis (requires API key)
- `POST /api/analyze` - Analyze with AI
- `POST /api/search-and-analyze` - Search and analyze results

### Utility
- `GET /api/health` - Health check
- `GET /api/history/searches` - Search history

## Configuration

### Required (for full functionality)
Set these in Space secrets:

1. **For Email Features**:
   - `SMTP_HOST` (default: smtp.gmail.com)
   - `SMTP_PORT` (default: 587)
   - `SMTP_USER` - Your email
   - `SMTP_PASSWORD` - Your email password/app password

2. **For AI Analysis Features**:
   - `OPENROUTER_API_KEY` - Get from https://openrouter.ai/

### Optional
- `DATABASE_PATH` - Database file path (default: ./database/agent_data.db)

## What Works Without API Keys

✅ Web Search (DuckDuckGo)
✅ News Search
✅ Data Storage
✅ Search History
❌ Email Sending (needs SMTP config)
❌ AI Analysis (needs OpenRouter key)

## Tech Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Search**: DuckDuckGo Search API
- **AI**: OpenRouter API (optional)
- **Frontend**: HTML, CSS, JavaScript

## Example Usage

### Search the Web
```bash
curl -X POST https://YOUR_SPACE_URL/api/search \
  -H "Content-Type: application/json" \
  -d '{"query": "Python programming", "max_results": 5}'
```

### Save Data
```bash
curl -X POST https://YOUR_SPACE_URL/api/save \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Note",
    "content": "Important information",
    "category": "notes"
  }'
```

## Local Development

```bash
cd backend
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`

## Project Structure

```
Multi-Tool Agent/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── agents/
│   │   ├── web_search_agent.py
│   │   ├── email_agent.py
│   │   └── openrouter_agent.py
│   ├── database/
│   │   └── db.py
│   └── requirements.txt
├── frontend/
│   └── index.html
└── Dockerfile
```

## Educational Purpose

This project demonstrates:
- Multi-agent architecture
- RESTful API design
- Database integration
- External API integration
- Error handling and logging
- Modular code structure
