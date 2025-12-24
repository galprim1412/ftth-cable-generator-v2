# Release Notes - v1.0.0

## 🎉 FTTH Cable Generator V2 - First Release

**Release Date:** December 24, 2025

### Overview

First production release of the FTTH Cable Generator - a modern, cross-platform desktop application for EMR fiber optic cable management. Built with Python and Tkinter, featuring a sleek dark theme UI.

---

## 📦 Downloads

Choose the version for your operating system:

| Platform | Download | Size | Requirements |
|----------|----------|------|--------------|
| 🪟 **Windows** | [EMR Cable Generator.exe](https://github.com/galprim1412/ftth-cable-generator-v2/releases/download/v1.0.0/EMR%20Cable%20Generator.exe) | ~10 MB | Windows 10/11 |
| 🍎 **macOS** | [EMR Cable Generator-macOS.zip](https://github.com/galprim1412/ftth-cable-generator-v2/releases/download/v1.0.0/EMR%20Cable%20Generator-macOS.zip) | ~12 MB | macOS 10.15+ |
| 🐧 **Linux** | [cable-generator](https://github.com/galprim1412/ftth-cable-generator-v2/releases/download/v1.0.0/cable-generator) | ~15 MB | Ubuntu 20.04+, Fedora 35+ |

---

## ✨ Features

### 1. Cable Generator
Generate standardized cable names for FTTH projects:
- **Cluster Cable:** `FDT - CABLE LINE [code] (FO [type]) - AE - [length] M`
- **Feeder Cable:** `OLT - FDT ([FEEDER_TYPE] CABLE FO [type]) - AE - [length] M`
  - Feeder Types: SUBFEEDER, HUBFEEDER, MAINFEEDER

**Supported Cable Types:**
- Cluster: 24C/2T, 36C/3T, 48C/4T
- Feeder: 24C/2T, 48C/4T, 96C/8T, 144C/12T, 288C/24T

### 2. Cluster Description Generator
Calculate cluster cable length with precision:
- Route distance (meters)
- Slack for FDT & FAT (units @ 20m each)
- Automatic 5% tolerance calculation
- OTDR comparison and variance

### 3. Feeder Description Generator
Calculate feeder cable length:
- Route distance (meters)
- Slack units (@ 20m each)
- Automatic 5% tolerance
- OTDR comparison and variance

---

## 🎨 UI Highlights

- ✅ Modern dark theme interface
- ✅ Tab-based navigation
- ✅ One-click copy to clipboard
- ✅ Custom application icon
- ✅ Centered window on startup
- ✅ Responsive button layout

---

## 📥 Installation Instructions

### Windows
1. Download `EMR Cable Generator.exe`
2. Double-click to run (no installation required)
3. If Windows Defender shows a warning, click "More info" → "Run anyway"

### macOS
1. Download `EMR Cable Generator-macOS.zip`
2. Extract the zip file
3. Move `EMR Cable Generator.app` to Applications folder
4. Right-click → Open (first time only to bypass Gatekeeper)

### Linux
1. Download `cable-generator`
2. Make executable: `chmod +x cable-generator`
3. Run: `./cable-generator`

---

## 🔧 Technical Details

- **Language:** Python 3.11+
- **GUI Framework:** Tkinter (built-in)
- **Build Tool:** PyInstaller 6.17.0
- **Lines of Code:** 611 lines
- **Dependencies:** None (standalone executables)

---

## 📊 Comparison with Previous Version

| Aspect | C Version | Python V2 |
|--------|-----------|-----------|
| Lines of Code | 786 | 611 |
| UI Layout | 3 separate windows | 3 tabs in one window |
| Compilation | Required | Not required (Python) |
| Dependencies | Win32 API | Python built-in only |
| Maintenance | Difficult | Easy |
| Theme | Default Windows | Modern dark theme |
| Cross-Platform | ❌ Windows only | ✅ Windows, macOS, Linux |

---

## 🚀 What's New in v1.0.0

### Core Features
- ✅ Complete rewrite in Python with modern UI
- ✅ Cross-platform support (Windows, macOS, Linux)
- ✅ Dark theme interface
- ✅ Tab-based navigation
- ✅ Copy to clipboard functionality

### Build & Distribution
- ✅ Automated multi-platform builds via GitHub Actions
- ✅ Single-file executables for easy distribution
- ✅ Custom application icon
- ✅ No installation required

### Documentation
- ✅ Comprehensive README with screenshots
- ✅ Detailed build guide (BUILD.md)
- ✅ Platform-specific installation instructions

---

## 🐛 Known Issues

None reported in this release.

---

## 📝 Usage Example

1. **Select Tab:** Choose Cable Generator, Cluster Description, or Feeder Description
2. **Fill Inputs:** Enter required parameters (code, type, length, etc.)
3. **Generate:** Click the blue GENERATE button
4. **Copy:** Use the green COPY button to copy result to clipboard
5. **Reset:** Click the red RESET button to clear all inputs

---

## 🔗 Links

- **Repository:** https://github.com/galprim1412/ftth-cable-generator-v2
- **Issues:** https://github.com/galprim1412/ftth-cable-generator-v2/issues
- **Documentation:** [README.md](https://github.com/galprim1412/ftth-cable-generator-v2#readme)
- **Build Guide:** [BUILD.md](https://github.com/galprim1412/ftth-cable-generator-v2/blob/main/docs/BUILD.md)

---

## 👨‍💻 Developer

Developed for EMR fiber optic cable management projects.

---

## 📄 License

Internal use - EMR Project

---

## 🙏 Acknowledgments

Special thanks to the Python and PyInstaller communities for making cross-platform development accessible.

---

**Enjoy using FTTH Cable Generator V2!** 🎊

If you encounter any issues, please report them on the [Issues page](https://github.com/galprim1412/ftth-cable-generator-v2/issues).
