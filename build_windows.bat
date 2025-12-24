@echo off
REM Windows Build Script for FTTH Cable Generator
REM This script builds a standalone .exe for Windows

echo ========================================
echo FTTH Cable Generator - Windows Build
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://www.python.org/
    pause
    exit /b 1
)

REM Check if PyInstaller is installed
python -c "import PyInstaller" >nul 2>&1
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
)

echo Building Windows executable...
echo.

REM Run PyInstaller
python -m PyInstaller --onefile --windowed --icon=app.ico --name="EMR Cable Generator" cable_generator_figma.py --clean

if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo ========================================
echo Output: dist\EMR Cable Generator.exe
echo.
pause
