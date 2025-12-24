# Build Guide - FTTH Cable Generator

This guide explains how to build the FTTH Cable Generator application for different operating systems.

## Prerequisites

### All Platforms
- Python 3.11 or higher
- pip (Python package installer)
- Git (for cloning the repository)

### Platform-Specific Requirements

**Windows:**
- No additional requirements

**macOS:**
- Xcode Command Line Tools: `xcode-select --install`

**Linux:**
- Development tools: `sudo apt-get install python3-dev python3-tk` (Ubuntu/Debian)
- Or: `sudo dnf install python3-devel python3-tkinter` (Fedora/RHEL)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/galprim1412/ftth-cable-generator-v2.git
cd ftth-cable-generator-v2
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Build for Your Platform

#### Windows

**Option 1: Using Python script**
```bash
python build.py
```

**Option 2: Using batch file**
```bash
build_windows.bat
```

Output: `dist/EMR Cable Generator.exe`

#### macOS

**Make script executable and run:**
```bash
chmod +x build_macos.sh
./build_macos.sh
```

Output: `dist/EMR Cable Generator.app`

#### Linux

**Make script executable and run:**
```bash
chmod +x build_linux.sh
./build_linux.sh
```

Output: `dist/cable-generator`

## Automated Builds (GitHub Actions)

The repository includes GitHub Actions workflows that automatically build for all platforms:

1. **Trigger builds:**
   - Push to `main` branch
   - Create a pull request
   - Manually via Actions tab

2. **Download builds:**
   - Go to: https://github.com/galprim1412/ftth-cable-generator-v2/actions
   - Click on the latest workflow run
   - Download artifacts for your platform

3. **Create a release:**
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
   This will automatically create a GitHub release with all platform builds attached.

## Build Customization

### Changing Application Name

Edit the build scripts and modify the `--name` parameter:

```python
# In build.py or build scripts
--name="Your Custom Name"
```

### Adding Application Icon

The application uses `app.ico` for the icon. To change it:

1. Replace `app.ico` with your icon file
2. For macOS, you may want to convert to `.icns` format
3. Rebuild the application

### Build Options

Common PyInstaller options you can add:

- `--onefile`: Single executable file (already used)
- `--windowed`: No console window (already used)
- `--add-data`: Include additional files
- `--hidden-import`: Include hidden imports
- `--exclude-module`: Exclude unnecessary modules

Example:
```bash
pyinstaller --onefile --windowed \
    --add-data "assets:assets" \
    --exclude-module matplotlib \
    cable_generator_figma.py
```

## Troubleshooting

### Windows

**Issue:** "Python is not recognized"
- **Solution:** Add Python to PATH or use full path to python.exe

**Issue:** Antivirus blocks the executable
- **Solution:** Add exception for the dist folder or sign the executable

### macOS

**Issue:** "App is damaged and can't be opened"
- **Solution:** Run `xattr -cr "dist/EMR Cable Generator.app"`

**Issue:** PyInstaller not found
- **Solution:** Use `pip3 install pyinstaller` instead of `pip`

### Linux

**Issue:** "tkinter module not found"
- **Solution:** Install python3-tk package for your distribution

**Issue:** Permission denied
- **Solution:** Run `chmod +x build_linux.sh` first

### All Platforms

**Issue:** Build fails with import errors
- **Solution:** Ensure all dependencies are installed: `pip install -r requirements.txt`

**Issue:** Large executable size
- **Solution:** Use `--exclude-module` to remove unused libraries

## Distribution

### Windows
- Distribute the `.exe` file directly
- Consider creating an installer with NSIS or Inno Setup

### macOS
- Distribute the `.app` bundle in a `.dmg` file
- Sign and notarize for Gatekeeper compatibility

### Linux
- Distribute the executable with installation instructions
- Consider creating `.deb` or `.rpm` packages
- Or use AppImage for universal compatibility

## Development Workflow

1. **Make changes** to `cable_generator_figma.py`
2. **Test locally** by running: `python cable_generator_figma.py`
3. **Build** using the appropriate script
4. **Test the executable** to ensure it works
5. **Commit and push** to trigger automated builds
6. **Create a tag** for releases

## Additional Resources

- [PyInstaller Documentation](https://pyinstaller.org/)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Python Packaging Guide](https://packaging.python.org/)
