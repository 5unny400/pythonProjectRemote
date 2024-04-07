"""
@FileName：pdf-split-div_zero_test.py
@Description：
@Author：shenxinyuan
@Time：2023/12/26
"""
def pdf_split(file_path: str) -> list:
    """
    pdf 拆分
    :param file_path: 多页PDF的文件路径
    :return: 拆分后的单页PDF文件路径列表，文件名格式 origin_name_0.pdf, origin_name_1.pdf ...
    """
    import os
    from PyPDF2 import PdfReader, PdfWriter
    folder, file_full_name = os.path.split(file_path)
    file_name, file_ext = file_full_name.rsplit('.', 1)[0], file_full_name.rsplit('.', 1)[1]
    reader = PdfReader(file_path)
    total_pages = reader.getNumPages()
    res = []
    for i in range(total_pages):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        new_file_full_name = "{}_{}.{}".format(file_name, str(i), file_ext)
        new_file_path = os.path.join(folder, new_file_full_name)
        with open(new_file_path, "wb") as fp:
            writer.write(fp)
        res.append(new_file_full_name)
    return res
