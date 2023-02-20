import os
from PyPDF2 import PdfFileMerger

target_path = r'需合并文件路径'
pdf_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf')]
pdf_lst = [os.path.join(target_path, filename) for filename in pdf_lst]

file_merger = PdfFileMerger()
for pdf in pdf_lst:
    file_merger.append(pdf)

file_merger.write(r"合并后文件存储路径/文件名称.pdf")
