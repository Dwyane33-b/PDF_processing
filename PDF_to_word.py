from pdf2docx import Converter
import easygui as eg


def convert(pdf_name, word_name):
    pdf_file = pdf_name
    docx_file = word_name
    # convert pdf to docx
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()


while 1:
    name = eg.multenterbox(title="输入文件路径", msg="输入需要转换及转换完成的文件路径", fields=['pdf文件路径', '转换后word文件路径'])
    convert(name[0], name[1])
