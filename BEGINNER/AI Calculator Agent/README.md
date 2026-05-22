# 🧮 AI Calculator Agent

A powerful AI-powered calculator that understands natural language math queries and provides detailed step-by-step solutions with memory capabilities.

![AI Calculator Agent](https://img.shields.io/badge/AI-Calculator-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Flask](https://img.shields.io/badge/Flask-3.0-red)
![OpenRouter](https://img.shields.io/badge/OpenRouter-API-purple)

## ✨ Features

### 🎯 Core Capabilities
- **Natural Language Processing**: Ask math questions in plain English
- **Advanced Math Operations**: 
  - Basic arithmetic (addition, subtraction, multiplication, division)
  - Power and exponents
  - Square roots and other roots
  - Trigonometric functions
  - Logarithms
- **Memory System**: Keeps track of all your calculations with timestamps
- **Structured Output**: Clear, organized results with:
  - Mathematical expression
  - Final answer
  - Step-by-step solution
  - Detailed explanation
- **Beautiful UI**: Modern, responsive design with dark theme
- **Quick Actions**: Pre-defined buttons for common operations

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- OpenRouter API key ([Get one here](https://openrouter.ai/))

### Installation

1. **Clone or download this project**
   ```bash
   cd "AI Calculator Agent"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   
   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📖 Usage

### Natural Language Queries
Simply type your math question in natural language:

- "What is 25 + 37?"
- "Calculate square root of 144"
- "What is 2 to the power of 8?"
- "Divide 144 by 12"
- "15 times 8"

### Quick Actions
Click any of the quick action buttons for instant calculations:
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🔢 Power
- √ Square Root

### Memory Features
- **View History**: All calculations are saved in the memory panel
- **Delete Individual**: Remove specific calculations
- **Clear All**: Wipe entire calculation history

## 🏗️ Project Structure

```
AI Calculator Agent/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── style.css         # Styling
    └── script.js         # Frontend JavaScript
```

## 🔧 Technical Details

### Backend (Flask)
- **Framework**: Flask 3.0
- **API Integration**: OpenRouter API with Claude 3.5 Sonnet
- **Features**:
  - RESTful API endpoints
  - In-memory calculation storage
  - Natural language processing
  - Structured JSON responses

### Frontend
- **Pure JavaScript**: No frameworks required
- **Responsive Design**: Works on all devices
- **Modern UI**: Dark theme with smooth animations
- **Real-time Updates**: Instant feedback and results

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main application page |
| `/calculate` | POST | Process calculation query |
| `/memory` | GET | Retrieve calculation history |
| `/memory/clear` | POST | Clear all history |
| `/memory/<id>` | DELETE | Delete specific calculation |

## 🎨 UI Features

- **Dark Theme**: Easy on the eyes
- **Gradient Accents**: Modern, professional look
- **Smooth Animations**: Polished user experience
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Icon Integration**: Font Awesome icons throughout

## 🔐 Security Notes

- Never commit your `.env` file
- Keep your OpenRouter API key private
- The `.gitignore` file is configured to exclude sensitive files

## 🐛 Troubleshooting

### API Key Issues
- Ensure your `.env` file exists and contains the correct key
- Verify the key format: `OPENROUTER_API_KEY=sk-or-v1-...`

### Port Already in Use
If port 5000 is busy, modify `app.py`:
```python
app.run(debug=True, port=5001)  # Change to any available port
```

### Module Not Found
Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

## 📝 Example Queries

```
"What is 156 + 289?"
"Calculate 15% of 200"
"Square root of 625"
"2 to the power of 10"
"What is 1000 divided by 25?"
"Calculate 12 times 13"
```

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements!

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- **OpenRouter**: For providing AI API access
- **Anthropic Claude**: For natural language processing
- **Font Awesome**: For beautiful icons
- **Flask**: For the web framework

---

**Made with ❤️ for the Nexe Agent Internship Program**
