---
title: AI Calculator Agent
emoji: 🧮
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# AI Calculator Agent 🧮

An intelligent calculator powered by AI that understands natural language math queries and provides step-by-step solutions.

## Features

- 🤖 **Natural Language Processing**: Ask math questions in plain English
- 📊 **Step-by-Step Solutions**: See detailed calculation steps
- 💾 **Memory System**: Keeps track of recent calculations
- 🎯 **Advanced Operations**: Supports basic arithmetic, powers, square roots, and more

## How to Use

1. Type your math question in natural language (e.g., "What is 25 + 37?")
2. Click "Calculate" or press Enter
3. View the result with detailed steps and explanation
4. Access calculation history in the memory panel

## Examples

- "What is 156 divided by 12?"
- "Calculate square root of 144"
- "15 times 8"
- "What is 2 to the power of 10?"

## Configuration

This app requires an OpenRouter API key. Set it in the Space secrets:
- Key name: `OPENROUTER_API_KEY`
- Get your key from: https://openrouter.ai/

## Tech Stack

- **Backend**: Flask (Python)
- **AI Model**: Meta Llama 3 8B via OpenRouter
- **Frontend**: HTML, CSS, JavaScript

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`
