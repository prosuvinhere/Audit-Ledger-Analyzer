#!/bin/bash
# Move into the directory where this script is located
cd "$(dirname "$0")"

echo "======================================================="
echo "    Starting Local Audit Ledger Analyzer Setup..."
echo "======================================================="
echo ""

# 1. Check if Python is installed (Macs usually use python3)
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed."
    echo "Please install Python from python.org and try again."
    exit 1
fi

# 2. Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "[WARNING] Ollama (Local AI Engine) is not installed."
    echo "Opening download page..."
    open https://ollama.com/download
    echo "Please download and install Ollama, then run this script again."
    exit 1
fi

# 3. Setup a local Virtual Environment
if [ ! -d "venv" ]; then
    echo "[INFO] First time setup: Creating local environment..."
    python3 -m venv venv
fi

# 4. Activate environment and install dependencies
source venv/bin/activate
echo "[INFO] Checking for required libraries..."
pip install -r requirements.txt -q

# 5. Download the AI Models (Pulls both for the UI toggle)
echo "[INFO] Ensuring local AI models are ready (this will take a moment on the first run)..."
echo "[INFO] Pulling Fast AI Model (approx 2GB)..."
ollama pull llama3.2:3b

echo "[INFO] Pulling Smart AI Model (approx 4.7GB)..."
ollama pull llama3.1

# 6. Launch the Streamlit App
echo ""
echo "======================================================="
echo "    Setup Complete! Launching the application..."
echo "    (Keep this terminal window open while using the app)"
echo "======================================================="
streamlit run app.py