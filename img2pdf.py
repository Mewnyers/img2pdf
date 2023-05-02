import os
import sys
from PIL import Image
from PyPDF2 import PdfMerger

# 引数の数を確認する
if len(sys.argv) < 2:
    print('Usage: python img2pdf.py [folder_path_or_file_path]')
    sys.exit(1)

# 引数からフォルダ名またはファイル名を取得する
input_path = sys.argv[1]

# フォルダが指定された場合
if os.path.isdir(input_path):
    # すべてのイメージファイルを.pdfに変換する
    for file_name in os.listdir(input_path):
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')):
            # PILでイメージファイルを開く
            img = Image.open(os.path.join(input_path, file_name))
            # .pdfに変換するために拡張子を変更
            pdf_path = os.path.join(input_path, os.path.splitext(file_name)[0] + '.pdf')
            # 保存する
            img.save(pdf_path, 'pdf')

    # フォルダ内のすべての.pdfを結合する
    merger = PdfMerger()
    for file_name in os.listdir(input_path):
        if file_name.endswith('.pdf'):
            file_path = os.path.join(input_path, file_name)
            merger.append(file_path)

    # 結合したpdfを保存する
    output_path = os.path.join(os.path.dirname(input_path), os.path.basename(input_path) + '.pdf')
    merger.write(output_path)
    merger.close()

    # .pdf以外のファイルを削除する
    for file_name in os.listdir(input_path):
        if file_name.endswith('.pdf'):
            pdf_path = os.path.join(input_path, file_name)
            image_ext = os.path.splitext(file_name)[0]
            for ext in ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp'):
                image_path = os.path.join(input_path, image_ext + ext)
                if os.path.exists(image_path):
                    os.remove(pdf_path)
                    break
    print('Conversion complete!')

# ファイルが指定された場合
elif os.path.isfile(input_path) and input_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff', '.webp')):
    # PILでイメージファイルを開く
    img = Image.open(input_path)
    # .pdfに変換するために拡張子を変更
    pdf_path = os.path.splitext(input_path)[0] + '.pdf'
    # 保存する
    img.save(pdf_path, 'pdf')
    print('Conversion complete!')

else:
    print('Usage: python img2pdf.py [folder_path_or_file_path]')
    sys.exit(1)
