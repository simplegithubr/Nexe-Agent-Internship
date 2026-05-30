@echo off
echo ========================================
echo RAG Assistant - Environment Setup
echo ========================================
echo.

cd backend

if exist ".env" (
    echo .env file already exists!
    echo.
    set /p overwrite="Do you want to overwrite it? (y/n): "
    if /i not "%overwrite%"=="y" (
        echo Setup cancelled.
        pause
        exit /b 0
    )
)

echo Creating .env file...
echo.

set /p api_key="Enter your OpenRouter API key: "

if "%api_key%"=="" (
    echo Error: API key cannot be empty!
    pause
    exit /b 1
)

echo OPENROUTER_API_KEY=%api_key% > .env

echo.
echo ✅ .env file created successfully!
echo.
echo Your configuration:
type .env
echo.
echo ========================================
echo Next steps:
echo 1. Run: start_backend.bat
echo 2. Open: frontend\index.html
echo ========================================
echo.
pause
