import os


def rename_files_in_directory(directory, old_suffix, new_suffix):
    for filename in os.listdir(directory):
        if filename.lower().endswith(old_suffix.lower()):
            new_filename = filename.replace(old_suffix, new_suffix)
            os.rename(
                os.path.join(directory, filename),
                os.path.join(directory, new_filename)
            )


# 使用示例
directory_path = r'D:/Administrator/图片'  # 替换为你的目录路径
rename_files_in_directory(directory_path, '.png', '.webp')  # 将所有.webp后缀改为.png后缀
