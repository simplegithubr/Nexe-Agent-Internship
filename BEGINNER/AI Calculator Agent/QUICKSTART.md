# 🚀 Quick Start Guide

## Step 1: Get Your OpenRouter API Key

1. Visit [OpenRouter.ai](https://openrouter.ai/)
2. Sign up or log in
3. Go to your API Keys section
4. Create a new API key
5. Copy the key (starts with `sk-or-v1-...`)

## Step 2: Configure Your API Key

Open the `.env` file and replace the placeholder:

```
OPENROUTER_API_KEY=sk-or-v1-your-actual-key-here
```

## Step 3: Run the Application

```bash
python app.py
```

## Step 4: Open in Browser

Navigate to: **http://localhost:5000**

---

## 🎯 Features Overview

### ✨ What You Can Do:

1. **Natural Language Queries**
   - "What is 25 + 37?"
   - "Calculate square root of 144"
   - "What is 2 to the power of 8?"

2. **Quick Action Buttons**
   - Click pre-defined operation buttons for instant calculations

3. **Memory System**
   - All calculations are automatically saved
   - View calculation history in the right panel
   - Delete individual calculations or clear all

4. **Structured Results**
   - See the mathematical expression
   - Get the final answer
   - View step-by-step solution
   - Read detailed explanation

---

## 🎨 UI Features

- **Dark Theme**: Professional and easy on the eyes
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Smooth Animations**: Polished user experience
- **Real-time Feedback**: Instant loading indicators and error messages

---

## 🔧 Troubleshooting

### "API key not configured" error
- Make sure you've added your OpenRouter API key to the `.env` file
- Restart the application after adding the key

### Port 5000 already in use
- Change the port in `app.py` (last line): `app.run(debug=True, port=5001)`

### Module not found errors
- Run: `pip install -r requirements.txt`

---

## 📝 Example Queries to Try

```
What is 156 + 289?
Calculate 15% of 200
Square root of 625
2 to the power of 10
What is 1000 divided by 25?
Calculate 12 times 13
What is 45 minus 18?
```

---

**Enjoy your AI Calculator Agent! 🎉**
