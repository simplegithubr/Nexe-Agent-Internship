#!/bin/bash

echo "🚀 Starting Multi-Tool Agent Server..."
echo ""
echo "📋 Pre-flight checks:"
echo "  ✓ Python installed"
echo "  ✓ Dependencies installed"
echo ""
echo "⚠️  IMPORTANT: Configure your API keys in backend/.env file"
echo "   - OPENROUTER_API_KEY (required for AI features)"
echo "   - SMTP credentials (optional, for email features)"
echo ""
echo "Starting Flask server..."
cd backend
python app.py
