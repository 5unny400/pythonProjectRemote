"""
@FileName：unpack_file_list.py
@Description：这是一个 Python 中的解包（unpacking）语法。假设 file_list 是一个包含多个文件对象的列表，而 src_file 是第一个文件对象，
tgt_file_list 是包含其余文件对象的列表。
@Author：shenxinyuan
@Time：2023/12/6
"""
# 假设 file_list 包含三个文件对象
# file_list = ["file1", "file2", "file3"]
file_list = ["file1", "file2"]

# 使用解包语法
src_file, *tgt_file_list = file_list

print(src_file)
print(tgt_file_list)
# 现在，src_file 包含 file1，tgt_file_list 包含 [file2, file3]
