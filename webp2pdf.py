import os
import sys
from PIL import Image
from PyPDF2 import PdfMerger

# 引数からフォルダ名を取得する
folder_name = sys.argv[1]

# フォルダ内の.webpをすべて.pdfに変換する
for file_name in os.listdir(folder_name):
    if file_name.endswith('.webp'):
        # PILで.webpを開く
        img = Image.open(os.path.join(folder_name, file_name))
        # .pdfに変換するために拡張子を変更
        pdf_path = os.path.join(folder_name, os.path.splitext(file_name)[0] + '.pdf')
        # 保存する
        img.save(pdf_path, 'pdf')

# フォルダ内のすべての.pdfを結合する
merger = PdfMerger()
for file_name in os.listdir(folder_name):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(folder_name, file_name)
        merger.append(file_path)
# 結合したpdfを保存する
output_path = folder_name + '.pdf'
merger.write(output_path)
merger.close()

# .pdf以外のファイルを削除する
for file_name in os.listdir(folder_name):
    if file_name.endswith('.pdf'):
        pdf_path = os.path.join(folder_name, file_name)
        webp_path = os.path.join(folder_name, os.path.splitext(file_name)[0] + '.webp')
        if os.path.exists(webp_path):
            os.remove(pdf_path)
print('Conversion complete!')
