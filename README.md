# webp2pdf
This is a simple Python script for converting multiple WebP image files to a single PDF file.

# Installation
To use this script, you need to have Python 3 and the PyPDF2 and Pillow libraries installed. You can install these libraries using pip:

```bash
pip install PyPDF2 Pillow
```

# Usage
Put all the WebP image files you want to convert into a folder. For example, let's say the folder name is `webp_files`.

Open the command prompt and navigate to the directory where the `webp2pdf.py` script is located.

Run the script with the following command:

```bash
python webp2pdf.py webp_files
```

Replace `webp_files` with the name of the folder that contains your WebP image files.

The script will convert all the WebP image files in the specified folder to PDF files, and then merge them into a single PDF file named `webp_files.pdf`. The newly created PDF file will be saved in the same folder as the WebP image files.

Finally, the script will delete all the PDF files that were created during the conversion process, except for the merged PDF file.

Alternatively, you can run the `run_converter.bat` file to launch the script without having to enter the command in the terminal.

# Limitations
This script is only designed to work with WebP image files. If you want to convert other image file formats to PDF, you will need to modify the script accordingly.