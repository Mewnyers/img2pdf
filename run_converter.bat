@echo off
set /p folder_name="Enter folder name to convert: "
python webp_to_pdf_converter.py "%folder_name%"
pause
