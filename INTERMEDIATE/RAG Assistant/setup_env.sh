#!/bin/bash

echo "========================================"
echo "RAG Assistant - Environment Setup"
echo "========================================"
echo ""

cd backend

if [ -f ".env" ]; then
    echo ".env file already exists!"
    echo ""
    read -p "Do you want to overwrite it? (y/n): " overwrite
    if [ "$overwrite" != "y" ]; then
        echo "Setup cancelled."
        exit 0
    fi
fi

echo "Creating .env file..."
echo ""

read -p "Enter your OpenRouter API key: " api_key

if [ -z "$api_key" ]; then
    echo "Error: API key cannot be empty!"
    exit 1
fi

echo "OPENROUTER_API_KEY=$api_key" > .env

echo ""
echo "✅ .env file created successfully!"
echo ""
echo "Your configuration:"
cat .env
echo ""
echo "========================================"
echo "Next steps:"
echo "1. Run: bash start_backend.sh"
echo "2. Open: frontend/index.html"
echo "========================================"
echo ""
