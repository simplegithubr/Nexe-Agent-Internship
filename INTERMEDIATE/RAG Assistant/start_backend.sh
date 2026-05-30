#!/bin/bash

echo "Starting RAG Assistant Backend..."
echo ""

cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

if [ ! -f ".env" ]; then
    echo ""
    echo "WARNING: .env file not found!"
    echo "Please create a .env file with your OPENROUTER_API_KEY"
    echo "Example: OPENROUTER_API_KEY=your_key_here"
    echo ""
    exit 1
fi

echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "Starting Flask server..."
python app.py
