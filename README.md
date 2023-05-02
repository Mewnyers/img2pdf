# img2pdf
img2pdf is a Python program that converts image files to PDF format. All images in a folder can be converted to PDF format and combined into a single PDF file.
It currently supports the following image formats: PNG, JPG, JPEG, WebP, BMP, GIF, TIFF

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
To convert a folder to PDF file:
```bash
python img2pdf.py [folder_path]
```

To convert a single image file to PDF file:
```bash
python img2pdf.py [image_file_path]
```

Alternatively, You can also start the script by drag-and-drop the folder or file you want to convert onto img2pdf.py without typing the command in the terminal.
