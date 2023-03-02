#!/bin/bash

# Setup backend
cd ./backend && \
# Use a virtual environment
python -m venv .backend && \
# Activate virtual environment
source .backend/bin/activate && \
# Load libraries for virtual environment
pip install -r requirement.txt && \
python main.py