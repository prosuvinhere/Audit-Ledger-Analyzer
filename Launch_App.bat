@echo off
TITLE Local Audit Ledger Analyzer
color 0A

echo =======================================================
echo     Starting Local Audit Ledger Analyzer Setup...
echo =======================================================
echo.

:: 1. Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed. 
    echo Please install Python from the Microsoft Store or python.org and try again.
    pause
    exit
)

:: 2. Check if Ollama is installed
ollama --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [WARNING] Ollama (Local AI Engine) is not installed.
    echo Opening download page...
    start https://ollama.com/download
    echo Please download and install Ollama, then run this script again.
    pause
    exit
)

:: 3. Setup a local Virtual Environment (Prevents messing with system Python)
IF NOT EXIST "venv" (
    echo [INFO] First time setup: Creating local environment...
    python -m venv venv
)

:: 4. Activate environment and install dependencies
call venv\Scripts\activate
echo [INFO] Checking for required libraries...
pip install -r requirements.txt -q

:: 5. Download the AI Models (Pulls both for the UI toggle)
echo [INFO] Ensuring local AI models are ready (this will take a moment on the first run)...
echo [INFO] Pulling Fast AI Model (approx 2GB)...
ollama pull llama3.2:3b

echo [INFO] Pulling Smart AI Model (approx 4.7GB)...
ollama pull llama3.1

:: 6. Launch the Streamlit App
echo.
echo =======================================================
echo     Setup Complete! Launching the application...
echo     (Keep this window open while using the app)
echo =======================================================
streamlit run app.py