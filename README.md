# Rename PDFs to Match Folder Names

This repository contains a Python script that automates the process of renaming PDF files within folders to match the respective folder names. It's a simple yet powerful tool for organizing files efficiently.

---

## Features
- Automatically renames PDF files to match the folder names they reside in.
- Skips files if a PDF with the target name already exists.
- Option to overwrite existing files (can be enabled in the script).
- Works for nested folders in a main directory.

---

## Usage

1. Clone or download the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/Rename-PDFs-to-Match-Folder-Names.git
   cd Rename-PDFs-to-Match-Folder-Names
   ```

2. Edit the `root_directory` variable in the script `rename_pdf.py` to point to the location of your main folder. Example:
   ```python
   root_directory = r"C:\path\to\your\main\folder"
   ```

3. Run the script:
   ```bash
   python rename_pdf.py
   ```

4. The script will process all folders and rename the PDF files accordingly.

---

## Requirements
- Python 3.x installed on your system.

---

## Example
### Before:
```
📂 Main Folder
 ├── 📂 Folder A
 │     └── file1.pdf
 ├── 📂 Folder B
 │     └── document.pdf
```

### After:
```
📂 Main Folder
 ├── 📂 Folder A
 │     └── Folder A.pdf
 ├── 📂 Folder B
 │     └── Folder B.pdf
```

---

## How It Works
1. The script reads all folders in the main directory.
2. For each folder, it finds the PDF file(s).
3. It renames the PDF to match the folder's name.
4. If a file with the target name already exists, the script skips or overwrites it based on configuration.


