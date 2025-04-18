#!/bin/bash

# Check if venv exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

# Optional: Install xdotool if on Linux
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if ! command -v xdotool &> /dev/null; then
        echo "xdotool not found. Installing..."
        sudo apt install -y xdotool
    fi
fi

echo "Starting Auto Key Spammer..."
python main.py
