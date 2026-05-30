@echo off
echo Starting RAG Assistant Backend...
echo.

cd backend

if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

if not exist ".env" (
    echo.
    echo WARNING: .env file not found!
    echo Please create a .env file with your OPENROUTER_API_KEY
    echo Example: OPENROUTER_API_KEY=your_key_here
    echo.
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting Flask server...
python app.py
