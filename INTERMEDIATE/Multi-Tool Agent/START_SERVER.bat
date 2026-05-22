@echo off
echo ========================================
echo   Multi-Tool Agent Server
echo ========================================
echo.
echo Starting server...
echo Server will run at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.
cd backend
python app.py
pause
