# FRENZ UTILS
A comprehensive Python package for processing and analyzing Frenz wearable device data. This package provides utilities for handling EEG, IMU, PPG, HR, and SPO2 sensor data.

## 🚀 Features

- Convert JSON files to CSV format
- Automatic CSV filename: `sessionId` + `_` + `__name__`
- CSV data has 2 columns: `timestamp` and `value`
- Extract data from the `values` array in the `result` object
- Auto-detect JSON files in current directory

## 🔧 Installation

### Prerequisites

**System Requirements:**
- Python 3.9 (required for compatibility)
- macOS (Intel/Apple Silicon) or Windows 64-bit
- Valid product key (contact Earable's sales department)

### Step 1: Install Python 3.9

**macOS:**
```bash
# Using Homebrew (recommended)
brew install python@3.9

# Or download from python.org
# https://www.python.org/downloads/release/python-3913/
```

**Windows:**
```bash
# Download from python.org
# https://www.python.org/ftp/python/3.9.13/python-3.9.13-amd64.exe
```

### Step 2: Create Virtual Environment

```bash
# Check Python version
python3.9 --version

# Create virtual environment
python3.9 -m venv vir_name

# Activate virtual environment
# macOS:
source vir_name/bin/activate

# Windows:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\vir_name\Scripts\Activate.ps1
```

### Step 3: Install Frenz Utils

**macOS Apple Silicon (M1/M2...):**
```bash
pip install frenz_utils-1.0.0-cp39-cp39-macosx_14_0_arm64.whl
```

**macOS Intel:**
```bash
pip install frenz_utils-1.0.0-cp39-cp39-macosx_10_9_universal2.whl
```

**Windows 64-bit:**
```bash
pip install frenz_utils-1.0.0-cp39-cp39-win_amd64.whl
```

### Step 4: Verify Installation

```python
import frenz_utils
print("✅ Frenz Utils installed successfully!")
```

## 🚀 Quick Start

### Convert JSON to CSV

```python
from frenz_utils.json_to_csv_converter import JsonToCsvConverter

converter = JsonToCsvConverter("your_product_key_here")
csv_file = converter.convert_json_to_csv("FOCUS_SCORE.json")
```

## 📖 Usage Examples

#### 1. `convert_json.py` - Convert JSON Files to CSV

**Purpose:** Convert JSON score files (FOCUS_SCORE, ALPHA_SCORE,...) to CSV format.

**Usage:**
```bash
# Run the script
python convert_json.py
```

**Features:**
- Automatically finds JSON files in current directory
- Supports single or multiple file conversion
- Provides conversion summary and performance metrics

**Output:**
- Creates CSV files with the same base name
- Maintains data structure and formatting

## 🛠️ Troubleshooting

### Common Issues

#### 1. "not a supported wheel on this platform"
**Cause:** Python version mismatch
**Solution:** Ensure you're using Python 3.9
```bash
python3.9 --version
python3.9 -m venv vir_name
source vir_name/bin/activate
```

#### 2. "No input was expected ($PIP_NO_INPUT set)"
**Cause:** Environment variable blocking pip prompts
**Solution:** Use `--yes` flag
```bash
pip uninstall frenz-utils --yes
```

#### 3. "Product key validation failed"
**Cause:** Invalid or missing product key
**Solution:** Contact Earable's sales department for a valid key

#### 4. "Source folder does not exist"
**Cause:** Incorrect path to raw data folder
**Solution:** Verify the folder path exists and contains sensor data

### Performance Optimization

- Use virtual environment with Python 3.9
- Ensure sufficient disk space for data processing
- Close other applications during large data processing
- Use SSD storage for better I/O performance

### Data Quality Checks

The tools include built-in data validation:
- NaN value detection
- Infinite value detection
- Timestamp consistency checks
- Data range validation

## 📞 Support

For technical support or product key requests:
- Contact: Earable's sales department
- Website: [https://frenzband.com/]

## 📄 License

This software is proprietary and requires a valid license to use.

---

**Note:** Always ensure you have a valid product key before using any functionality. The product key is required for data decryption and processing.
