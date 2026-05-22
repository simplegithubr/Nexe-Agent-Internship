# Web UI Usage Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install flask
```

### 2. Start the Web Server
```bash
python app.py
```

### 3. Open in Browser
Navigate to: **http://localhost:5000**

---

## 📋 Features

### ✅ Implemented Features

1. **Function Calling** ✓
   - 4 built-in tools (Calculator, Time, Weather, Text Analyzer)
   - Easy to add custom tools
   - Proper error handling

2. **JSON Response Format** ✓
   - All responses in structured JSON
   - Success/error status
   - Timestamps and metadata

3. **Error Handling** ✓
   - Try-catch blocks in all tools
   - Meaningful error messages
   - Error type identification

4. **Web UI** ✓
   - Modern dark theme interface
   - Real-time results display
   - Command history tracking
   - Responsive design

---

## 🎯 Available Tools

### 1. Calculator
- **Operations**: Add, Subtract, Multiply, Divide
- **Input**: Two numbers
- **Example**: `10 + 5 = 15`

### 2. Get Time
- Returns current date, time, and day
- No input required

### 3. Weather
- **Input**: City name
- **Available Cities**: Karachi, Lahore, Islamabad, London, New York
- Returns temperature, condition, humidity

### 4. Text Analyzer
- **Input**: Any text
- Returns word count, character count, sentences, etc.

---

## 🔌 API Endpoints

### GET `/`
Main web interface

### GET `/api/tools`
Get list of available tools

### POST `/api/call`
Generic tool calling endpoint
```json
{
  "tool": "calculator",
  "params": {
    "operation": "add",
    "num1": 10,
    "num2": 5
  }
}
```

### POST `/api/calculator`
```json
{
  "operation": "add",
  "num1": 10,
  "num2": 5
}
```

### GET `/api/time`
No parameters required

### POST `/api/weather`
```json
{
  "city": "Karachi"
}
```

### POST `/api/analyze`
```json
{
  "text": "Hello World"
}
```

### GET `/health`
Health check endpoint

---

## 🤖 Adding OpenRouter Integration (Optional)

If you want AI-powered tool selection using OpenRouter:

### 1. Install OpenRouter SDK
```bash
pip install openai  # OpenRouter uses OpenAI SDK
```

### 2. Get API Key
- Sign up at https://openrouter.ai
- Get your API key

### 3. Create `.env` file
```
OPENROUTER_API_KEY=your_api_key_here
```

### 4. Add AI Agent (create `ai_agent.py`)
```python
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def ai_tool_selector(user_query):
    """Use AI to select appropriate tool based on user query"""
    
    tools_description = """
    Available tools:
    1. calculator - for math operations (add, subtract, multiply, divide)
    2. get_time - to get current date and time
    3. weather - to check weather for a city
    4. text_analyzer - to analyze text statistics
    """
    
    response = client.chat.completions.create(
        model="anthropic/claude-3.5-sonnet",
        messages=[
            {"role": "system", "content": f"You are a tool selector. {tools_description}"},
            {"role": "user", "content": f"Which tool should I use for: {user_query}"}
        ]
    )
    
    return response.choices[0].message.content
```

---

## 📝 Testing

### Test via Web UI
1. Open http://localhost:5000
2. Select a tool
3. Enter parameters
4. Click execute button

### Test via API (using curl)
```bash
# Calculator
curl -X POST http://localhost:5000/api/calculator \
  -H "Content-Type: application/json" \
  -d '{"operation":"add","num1":10,"num2":5}'

# Time
curl http://localhost:5000/api/time

# Weather
curl -X POST http://localhost:5000/api/weather \
  -H "Content-Type: application/json" \
  -d '{"city":"Karachi"}'

# Text Analyzer
curl -X POST http://localhost:5000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text":"Hello World"}'
```

---

## 🎨 UI Features

- **Dark Theme**: Modern, eye-friendly design
- **Real-time Results**: Instant feedback
- **History Tracking**: Last 10 operations saved
- **Local Storage**: History persists across sessions
- **Responsive**: Works on mobile and desktop

---

## 🔧 Customization

### Add New Tool
Edit `agent.py`:
```python
def my_custom_tool(self, param1: str) -> Dict[str, Any]:
    """Your custom tool"""
    try:
        # Your logic here
        return {
            "success": True,
            "result": "your_result"
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Register in __init__
self.register_tool("my_tool", self.my_custom_tool)
```

Then add UI in `templates/index.html` and `static/script.js`

---

## 📊 Project Structure

```
Tool-Calling AI Agent/
├── agent.py              # Core agent with tools
├── app.py                # Flask web server
├── cli.py                # Command-line interface
├── examples.py           # Usage examples
├── test_agent.py         # Unit tests
├── requirements.txt      # Dependencies
├── templates/
│   └── index.html       # Web UI HTML
└── static/
    ├── style.css        # Styling
    └── script.js        # Frontend logic
```

---

## ✅ Verification Checklist

- [x] Function calling implemented
- [x] JSON response format
- [x] Error handling
- [x] Web UI created
- [x] API endpoints working
- [x] History tracking
- [ ] OpenRouter integration (optional)
- [ ] Custom tools added (optional)

---

## 🚀 Next Steps

1. **Test the web UI** - Open http://localhost:5000
2. **Try all tools** - Calculator, Time, Weather, Text Analyzer
3. **Check error handling** - Try invalid inputs
4. **Add OpenRouter** (optional) - For AI-powered tool selection
5. **Add custom tools** - Extend functionality

---

## 📞 Support

For issues or questions:
- Check the console for error messages
- Verify Flask is installed: `pip install flask`
- Ensure port 5000 is not in use
- Check browser console (F12) for frontend errors
