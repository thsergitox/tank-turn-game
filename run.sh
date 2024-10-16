#!/bin/bash

# Create grafana_data directory
mkdir -p grafana_data

# Build and start Docker containers
docker compose up --build -d

# Check if Docker containers are running
if [ $? -ne 0 ]; then
    echo "Failed to start Docker containers."
    exit 1
fi

# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt

# Check if dependencies were installed successfully
if [ $? -ne 0 ]; then
    echo "Failed to install dependencies."
    deactivate
    exit 1
fi

# Run the game
python3 src/app/main.py

# Deactivate the virtual environment
deactivate