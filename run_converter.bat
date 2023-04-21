@echo off
set /p folder_name="Enter folder name to convert: "
python webp2pdf.py "%folder_name%"
pause
