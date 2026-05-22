@echo off
echo Testing Multi-Tool Agent Server...
echo.
cd backend
echo Starting server...
timeout /t 2 /nobreak >/dev/null
start /min python app.py
timeout /t 5 /nobreak >/dev/null
echo.
echo Opening browser...
start http://localhost:5000
echo.
echo Server started! Check your browser.
echo Press any key to stop the server...
pause >/dev/null
taskkill /F /IM python.exe /FI "WINDOWTITLE eq *app.py*" 2>/dev/null
echo Server stopped.
