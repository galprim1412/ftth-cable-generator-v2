#!/bin/bash
# Linux Build Script for FTTH Cable Generator
# This script builds a standalone executable for Linux

echo "========================================"
echo "FTTH Cable Generator - Linux Build"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.11+ using your package manager"
    exit 1
fi

echo "Python version:"
python3 --version
echo ""

# Check if PyInstaller is installed
if ! python3 -c "import PyInstaller" &> /dev/null; then
    echo "PyInstaller not found. Installing..."
    pip3 install pyinstaller
fi

echo "Building Linux executable..."
echo ""

# Run PyInstaller
python3 -m PyInstaller \
    --onefile \
    --windowed \
    --name=cable-generator \
    cable_generator_figma.py \
    --clean

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "Build completed successfully!"
    echo "========================================"
    echo "Output: dist/cable-generator"
    echo ""
    echo "To run the executable:"
    echo "  chmod +x dist/cable-generator"
    echo "  ./dist/cable-generator"
    echo ""
    
    # Make executable
    chmod +x dist/cable-generator
    echo "Executable permissions set."
    echo ""
else
    echo ""
    echo "ERROR: Build failed!"
    exit 1
fi
