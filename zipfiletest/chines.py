"""
@FileName：chines.py
@Description：
@Author：shenxinyuan
@Time：2023/12/26
"""
import zipfile


def support_gbk(zip_file: zipfile.ZipFile):
    name_to_info = zip_file.NameToInfo
    for name, info in name_to_info.copy().items():
        real_name = name.encode('cp437').decode('gbk')
        if real_name != name:
            info.filename = real_name
            del name_to_info[name]
            name_to_info[real_name] = info
    return zip_file


# 使用
zf_path = ""
zipFile = support_gbk(zipfile.ZipFile(zf_path, "r"))