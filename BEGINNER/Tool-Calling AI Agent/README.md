# Tool-Calling AI Agent - Beginner Guide

## 📚 Concepts Explained (Urdu/English)

### 1️⃣ Function Calling (Tool Calling)

**Kya hai?**
- Function calling ka matlab hai ke aapka AI agent different functions/tools ko call kar sakta hai
- Jaise ek calculator, weather checker, ya text analyzer
- Agent decide karta hai ke konsa tool use karna hai based on user ki request

**Kaise kaam karta hai?**
```python
# Tool register karo
agent.register_tool("calculator", calculator_function)

# Tool ko call karo
result = agent.call_tool("calculator", operation="add", num1=5, num2=3)
```

**Benefits:**
- ✅ Modular code - har tool alag hai
- ✅ Easy to add new tools
- ✅ Reusable functions

---

### 2️⃣ JSON Response

**Kya hai?**
- JSON (JavaScript Object Notation) ek standard format hai data exchange ke liye
- Structured data return karta hai jo easily parse ho sakta hai
- Human-readable aur machine-readable dono

**Example Response:**
```json
{
  "success": true,
  "result": 15,
  "operation": "add",
  "tool_name": "calculator",
  "timestamp": "2026-05-13T10:30:00"
}
```

**Benefits:**
- ✅ Consistent format
- ✅ Easy to parse
- ✅ Contains metadata
- ✅ Works with APIs

---

### 3️⃣ Error Handling

**Kya hai?**
- Errors ko gracefully handle karna
- User ko clear error messages dena
- Program crash na ho

**Types of Errors Handled:**

1. **Invalid Tool Name**
```json
{
  "success": false,
  "error": "Tool 'xyz' not found",
  "available_tools": ["calculator", "weather", "get_time"]
}
```

2. **Wrong Arguments**
```json
{
  "success": false,
  "error": "Invalid arguments: missing num2",
  "error_type": "TypeError"
}
```

3. **Business Logic Errors**
```json
{
  "success": false,
  "error": "Cannot divide by zero",
  "error_type": "ValueError"
}
```

**Benefits:**
- ✅ Program crash nahi hota
- ✅ Clear error messages
- ✅ Easy debugging
- ✅ Better user experience

---

## 🚀 Quick Start

### Installation

```bash
# Python 3.7+ required
python --version

# No external dependencies needed for basic version
```

### Run the Demo

```bash
python agent.py
```

---

## 📖 Code Structure

```
agent.py
├── ToolCallingAgent (Main Class)
│   ├── __init__()              # Initialize agent
│   ├── register_tool()         # Add new tools
│   ├── call_tool()             # Execute tools
│   ├── calculator_tool()       # Math operations
│   ├── get_time_tool()         # Current time
│   ├── weather_tool()          # Weather info
│   └── text_analyzer_tool()    # Text analysis
└── main()                      # Demo function
```

---

## 🛠️ Available Tools

### 1. Calculator
```python
agent.call_tool("calculator", 
    operation="add",  # add, subtract, multiply, divide
    num1=10, 
    num2=5
)
```

### 2. Get Time
```python
agent.call_tool("get_time")
```

### 3. Weather
```python
agent.call_tool("weather", city="Karachi")
# Available: Karachi, Lahore, Islamabad, London, New York
```

### 4. Text Analyzer
```python
agent.call_tool("text_analyzer", 
    text="Your text here"
)
```

---

## 🎯 How to Add Your Own Tool

```python
def my_custom_tool(self, param1: str, param2: int) -> Dict[str, Any]:
    """
    Your tool description
    
    Args:
        param1: Description
        param2: Description
    """
    try:
        # Your logic here
        result = param1 * param2
        
        return {
            "success": True,
            "result": result,
            "custom_data": "anything you want"
        }
    
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "error_type": type(e).__name__
        }

# Register it
agent.register_tool("my_tool", agent.my_custom_tool)
```

---

## 🧪 Testing

The `main()` function includes 7 test cases:
1. ✅ Basic calculator operation
2. ✅ Get current time
3. ✅ Weather lookup
4. ✅ Text analysis
5. ❌ Invalid tool name (error handling)
6. ❌ Missing arguments (error handling)
7. ❌ Division by zero (error handling)

---

## 📝 Key Learnings

### Function Calling
- Tools ko dynamically register kar sakte hain
- Dictionary mein store karte hain
- Runtime pe call kar sakte hain

### JSON Response
- Always consistent structure return karo
- `success` field se check karo operation successful tha ya nahi
- Metadata add karo (timestamp, tool_name, etc.)

### Error Handling
- Try-except blocks use karo
- Specific error types catch karo
- User-friendly error messages do
- Never crash the program

---

## 🔥 Next Steps

1. **Add More Tools:**
   - File operations
   - Database queries
   - API calls
   - Image processing

2. **Add AI Integration:**
   - Use OpenAI/Claude API
   - Let AI decide which tool to use
   - Natural language to tool mapping

3. **Add Logging:**
   - Track all tool calls
   - Monitor performance
   - Debug issues

4. **Add Authentication:**
   - API keys for tools
   - User permissions
   - Rate limiting

---

## 💡 Common Issues & Solutions

### Issue 1: Tool not found
```python
# Solution: Check available tools
print(agent.get_available_tools())
```

### Issue 2: Wrong arguments
```python
# Solution: Check tool documentation
print(agent.get_tool_info())
```

### Issue 3: Unexpected errors
```python
# Solution: Check the error_type in response
if not result["success"]:
    print(f"Error: {result['error']}")
    print(f"Type: {result['error_type']}")
```

---

## 📚 Resources

- Python Type Hints: https://docs.python.org/3/library/typing.html
- JSON in Python: https://docs.python.org/3/library/json.html
- Error Handling: https://docs.python.org/3/tutorial/errors.html

---

## 🤝 Contributing

Apne tools add karna chahte hain? Simple steps:
1. New tool function banao
2. Error handling add karo
3. JSON response return karo
4. Register karo

---

## ✨ Author

Built for learning purposes - Tool-Calling AI Agent
Date: May 2026
