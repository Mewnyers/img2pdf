# webp2pdf
webp2pdf is a Python script that converts all WebP images in a folder to PDF format, and then merges them into a single PDF file. It can also convert a single WebP image file to PDF.

# Requirements
・Python 3.x
・Pillow (Python Imaging Library)
・PyPDF2

# Installation
To use this script, you need to have Python 3 and the PyPDF2 and Pillow libraries installed. You can install these libraries using pip:
```bash
pip install PyPDF2 Pillow
```

# Usage
To convert a folder of WebP images to a PDF file:
```bash
python webp2pdf.py [folder_path]
```

To convert a single WebP image file to a PDF file:
```bash
python webp2pdf.py [file_path]
```

Alternatively, You can also start the script by drag-and-drop the folder or file you want to convert onto webp2pdf.py without typing the command in the terminal.