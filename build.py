#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universal build script for FTTH Cable Generator
Automatically detects OS and builds appropriate executable
"""

import os
import sys
import platform
import subprocess
import shutil

def get_platform():
    """Detect current platform"""
    system = platform.system().lower()
    if system == 'windows':
        return 'windows'
    elif system == 'darwin':
        return 'macos'
    elif system == 'linux':
        return 'linux'
    else:
        return 'unknown'

def clean_build():
    """Clean previous build artifacts"""
    print("🧹 Cleaning previous build artifacts...")
    dirs_to_clean = ['build', 'dist', '__pycache__']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Removed {dir_name}/")
    
    # Remove .spec files
    for file in os.listdir('.'):
        if file.endswith('.spec'):
            os.remove(file)
            print(f"   Removed {file}")

def build_windows():
    """Build Windows executable"""
    print("🪟 Building for Windows...")
    
    # Check if icon file exists
    if not os.path.exists('app.ico'):
        print("⚠️  Warning: app.ico not found, building without icon")
        cmd = [
            sys.executable, '-m', 'PyInstaller',
            '--onefile',
            '--windowed',
            '--name=EMR Cable Generator',
            'cable_generator_figma.py',
            '--clean'
        ]
    else:
        print("✅ Icon file found")
        cmd = [
            sys.executable, '-m', 'PyInstaller',
            '--onefile',
            '--windowed',
            '--icon=app.ico',
            '--name=EMR Cable Generator',
            'cable_generator_figma.py',
            '--clean'
        ]
    
    subprocess.run(cmd, check=True)
    print("✅ Windows build complete: dist/EMR Cable Generator.exe")

def build_macos():
    """Build macOS application bundle"""
    print("🍎 Building for macOS...")
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--windowed',
        '--name=EMR Cable Generator',
        'cable_generator_figma.py',
        '--clean',
        '--osx-bundle-identifier=com.emr.cablegenerator'
    ]
    subprocess.run(cmd, check=True)
    print("✅ macOS build complete: dist/EMR Cable Generator.app")

def build_linux():
    """Build Linux executable"""
    print("🐧 Building for Linux...")
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--onefile',
        '--windowed',
        '--name=cable-generator',
        'cable_generator_figma.py',
        '--clean'
    ]
    subprocess.run(cmd, check=True)
    print("✅ Linux build complete: dist/cable-generator")

def main():
    """Main build process"""
    print("=" * 60)
    print("FTTH Cable Generator - Universal Build Script")
    print("=" * 60)
    
    current_platform = get_platform()
    print(f"📍 Detected platform: {current_platform}")
    
    if current_platform == 'unknown':
        print("❌ Unsupported platform!")
        sys.exit(1)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print(f"✅ PyInstaller version: {PyInstaller.__version__}")
    except ImportError:
        print("❌ PyInstaller not found!")
        print("   Install it with: pip install pyinstaller")
        sys.exit(1)
    
    # Clean previous builds
    clean_build()
    
    # Build for current platform
    print()
    try:
        if current_platform == 'windows':
            build_windows()
        elif current_platform == 'macos':
            build_macos()
        elif current_platform == 'linux':
            build_linux()
        
        print()
        print("=" * 60)
        print("🎉 Build completed successfully!")
        print("=" * 60)
        print(f"📦 Output location: dist/")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
