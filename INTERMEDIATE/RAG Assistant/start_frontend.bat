@echo off
echo Starting RAG Assistant Frontend...
echo.

cd frontend

echo Opening frontend in default browser...
start index.html

echo.
echo Alternative: Run a local server
echo python -m http.server 8080
echo Then visit: http://localhost:8080
echo.
pause
