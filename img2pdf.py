import os
import sys
from typing import List
from PIL import Image
from PyPDF2 import PdfMerger

def main(input_paths: List[str]) -> None:
    """
    画像ファイルまたはフォルダをPDFに変換し、PDFを結合する。
    """
    for input_path in input_paths:
        if os.path.isdir(input_path):
            convert_folder_to_pdf(input_path)
        elif os.path.isfile(input_path) and is_image_file(input_path):
            convert_file_to_pdf(input_path)
        else:
            print(f'Invalid input path: {input_path}')

def convert_folder_to_pdf(folder_path: str) -> None:
    """
    フォルダ内の画像ファイルをPDFに変換し、PDFを結合する。
    """
    image_files = get_image_files(folder_path)
    if not image_files:
        print(f'No image files found in {folder_path}')
        return

    pdf_files = []
    for image_file in image_files:
        pdf_file = convert_image_to_pdf(image_file)
        pdf_files.append(pdf_file)

    output_path = os.path.join(os.path.dirname(folder_path), os.path.basename(folder_path) + '.pdf')
    merge_pdfs(pdf_files, output_path)
    delete_non_pdf_files(folder_path)

    print(f'Conversion complete for {folder_path}!')

def convert_file_to_pdf(file_path: str) -> None:
    """
    画像ファイルをPDFに変換する。
    """
    pdf_file = convert_image_to_pdf(file_path)
    print(f'Conversion complete for {file_path}!')

def get_image_files(folder_path: str) -> List[str]:
    """
    フォルダ内の画像ファイルのリストを取得する。
    """
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')
    image_files = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path) if file_name.lower().endswith(image_extensions)]
    return image_files

def is_image_file(file_path: str) -> bool:
    """
    画像ファイルかどうかを判定する。
    """
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')
    return file_path.lower().endswith(image_extensions)

def convert_image_to_pdf(image_file: str) -> str:
    """
    画像ファイルをPDFに変換する。
    """
    pdf_file = os.path.splitext(image_file)[0] + '.pdf'
    with Image.open(image_file) as img:
        img.save(pdf_file, 'pdf')
    return pdf_file

def merge_pdfs(pdf_files: List[str], output_path: str) -> None:
    """
    PDFファイルを結合する。
    """
    merger = PdfMerger()
    for pdf_file in pdf_files:
        merger.append(pdf_file)
    merger.write(output_path)
    merger.close()

def delete_non_pdf_files(folder_path: str) -> None:
    """
    PDF以外のファイルを削除する。
    """
    pdf_files = [file_name for file_name in os.listdir(folder_path) if file_name.endswith('.pdf')]
    for pdf_file in pdf_files:
        image_file = os.path.splitext(pdf_file)[0]
        for ext in ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp'):
            image_path = os.path.join(folder_path, image_file + ext)
            if os.path.exists(image_path):
                os.remove(os.path.join(folder_path, pdf_file))
                break

if __name__ == '__main__':
    # 引数の数を確認する
    if len(sys.argv) < 2:
        print('Usage: python img2pdf.py [folder_path_or_file_path]')
        sys.exit(1)

    input_paths = sys.argv[1:]
    main(input_paths)
