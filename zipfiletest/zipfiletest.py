"""
@FileName：zipfiletest.py
@Description：
@Author：shenxinyuan
@Time：2023/12/26
"""
import zipfile
import os
import shutil

zf_path = "zip_file_path"
target_dir = ""

# zipFile = support_gbk(zipfile.ZipFile(zf_path, 'r'))
zipFile = zipfile.ZipFile(zf_path, 'r')

for file_m in zipFile.namelist():
    # data = zipFile.read(file_m)
    # (lambda f, d: (f.write(d), f.close()))(open(target_file_path, 'w'), data.decode('utf-8', 'ignore'))
    try:
        zipFile.extract(file_m, target_dir)
    except zipfile.BadZipFile as bzf:
        print(bzf)

zipFile.close()