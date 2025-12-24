#!/bin/bash
# macOS Build Script for FTTH Cable Generator
# This script builds a standalone .app bundle for macOS

echo "========================================"
echo "FTTH Cable Generator - macOS Build"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.11+ from https://www.python.org/"
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

echo "Building macOS application bundle..."
echo ""

# Run PyInstaller
python3 -m PyInstaller \
    --onefile \
    --windowed \
    --icon=app.ico \
    --name="EMR Cable Generator" \
    --osx-bundle-identifier=com.emr.cablegenerator \
    cable_generator_figma.py \
    --clean

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================"
    echo "Build completed successfully!"
    echo "========================================"
    echo "Output: dist/EMR Cable Generator.app"
    echo ""
    echo "To run the app:"
    echo "  open 'dist/EMR Cable Generator.app'"
    echo ""
else
    echo ""
    echo "ERROR: Build failed!"
    exit 1
fi
