---
title: Tool-Calling AI Agent
emoji: 🛠️
colorFrom: green
colorTo: blue
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# Tool-Calling AI Agent 🛠️

A beginner-friendly AI agent that demonstrates tool-calling capabilities with multiple built-in tools.

## Features

- 🧮 **Calculator**: Perform basic math operations (add, subtract, multiply, divide)
- ⏰ **Time Tool**: Get current date and time
- 🌤️ **Weather Tool**: Get simulated weather information for cities
- 📝 **Text Analyzer**: Analyze text for word count, character count, and more

## Available Tools

### 1. Calculator
Perform mathematical operations:
- Addition
- Subtraction
- Multiplication
- Division

### 2. Get Time
Returns current date and time in multiple formats.

### 3. Weather
Get weather information for any city (simulated data for demo purposes).

### 4. Text Analyzer
Analyze text and get:
- Word count
- Character count
- Sentence count
- Average word length

## How to Use

1. Select a tool from the dropdown
2. Fill in the required parameters
3. Click "Call Tool"
4. View the JSON response

## API Endpoints

- `GET /` - Web interface
- `GET /api/tools` - List all available tools
- `POST /api/call` - Call any tool with parameters
- `POST /api/calculator` - Direct calculator endpoint
- `GET /api/time` - Direct time endpoint
- `POST /api/weather` - Direct weather endpoint
- `POST /api/analyze` - Direct text analyzer endpoint
- `GET /health` - Health check

## Example API Call

```bash
curl -X POST https://YOUR_SPACE_URL/api/call \
  -H "Content-Type: application/json" \
  -d '{
    "tool": "calculator",
    "params": {
      "operation": "add",
      "num1": 10,
      "num2": 20
    }
  }'
```

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **No external AI API required** - Pure Python implementation

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`

## Educational Purpose

This project is designed for beginners to understand:
- How AI agents work
- Tool-calling patterns
- JSON-based communication
- RESTful API design
