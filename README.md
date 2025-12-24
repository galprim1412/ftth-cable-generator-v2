# EMR Cable Generator Tools

Modern cable generator application for EMR fiber optic projects with dark theme UI.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-Internal-red)

## 🎯 Features

### 1. Cable Generator
Generate cable names for two types:
- **Cluster Cable**: `FDT - CABLE LINE [code] (FO [type]) - AE - [length] M`
- **Feeder Cable**: `OLT - FDT ([FEEDER_TYPE] CABLE FO [type]) - AE - [length] M`
  - Feeder Types: SUBFEEDER, HUBFEEDER, MAINFEEDER

### 2. Cluster Description Generator
Calculate cluster cable length with:
- Route (meters)
- Slack FDT & FAT (units @ 20m each)
- 5% tolerance
- OTDR comparison

### 3. Feeder Description Generator
Calculate feeder cable length with:
- Route (meters)
- Slack (units @ 20m)
- 5% tolerance
- OTDR comparison

## 📦 Installation

### Option 1: Run from Source
```bash
# Clone repository
git clone https://github.com/galprim1412/ftth-cable-generator-v2.git
cd ftth-cable-generator-v2

# Run application
python cable_generator_figma.py
```

**Requirements:**
- Python 3.11+
- tkinter (built-in)

### Option 2: Use Executable
Download the latest release and run `EMR Cable Generator.exe` directly.

## 🔨 Building Executable

To build your own .exe file:

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
python -m PyInstaller --onefile --windowed --icon=app.ico --name="EMR Cable Generator" cable_generator_figma.py --clean
```

Output will be in `dist/EMR Cable Generator.exe`

## 🎨 UI Features

- ✅ Modern dark theme
- ✅ Centered window on startup
- ✅ Custom application icon
- ✅ Responsive button spacing
- ✅ Tab-based navigation
- ✅ Copy to clipboard functionality

## 📊 Comparison with C Version

| Aspect | C Version | Python Version |
|--------|-----------|----------------|
| Lines of Code | 786 | 597 |
| UI Layout | 3 separate tabs | 3 tabs in one window |
| Compilation | Required | Not required |
| Dependencies | Win32 API | Python built-in only |
| Maintenance | Difficult | Easy |
| Theme | Default Windows | Modern dark theme |

## 🚀 Usage

1. **Select Tab**: Choose Cable Generator, Cluster Description, or Feeder Description
2. **Fill Inputs**: Enter required parameters
3. **Generate**: Click GENERATE button
4. **Copy**: Use COPY button to copy result to clipboard
5. **Reset**: Click RESET to clear all inputs

## 📝 Cable Types

**Cluster Cable:**
- 24C/2T
- 36C/3T
- 48C/4T

**Feeder Cable:**
- 24C/2T
- 48C/4T
- 96C/8T
- 144C/12T
- 288C/24T

## 🛠️ Development

Project structure:
```
cable-generator-v2/
├── cable_generator_figma.py    # Main application
├── app.ico                      # Application icon
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## 📄 License

Internal use - EMR Project

## 👨‍💻 Author

Developed for EMR fiber optic cable management
