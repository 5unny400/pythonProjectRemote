from PIL import Image
import os


def convert_webp_to_png(source_directory_path, target_directory_path):
    index = 1
    cnt = 0
    for filename in os.listdir(source_directory_path):
        cnt += 1
        if filename.endswith('.webp'):
            webp_file = os.path.join(source_directory_path, filename)
            png_file = os.path.join(target_directory_path, filename.replace('.webp', '.png'))
            try:
                # 打开 WebP 格式的图片
                with Image.open(webp_file) as img:
                    # 转换为 RGB 模式（避免包含 alpha 通道）
                    img = img.convert('RGB')
                    # 保存为 PNG 格式的图片到指定路径

                    img.save(png_file, 'PNG')
                    print(f"{index }+{webp_file}+已修改为png格式！")
                # 删除原始的 WebP 格式图片
                os.remove(webp_file)
                index += 1
            except Exception as e:
                print(f"Error converting {webp_file}: {e}")
    print(f"一共遍历了{cnt}张图片。")


def rename_files(directory_path):
    file_num = 1
    for filename in os.listdir(directory_path):
        if filename.endswith('.png'):
            file_num += 1
            new_filename = f"{file_num}.png"
            os.rename(os.path.join(directory_path, filename), os.path.join(directory_path, new_filename))
            print(f"已将{filename}重命名为{new_filename}")



# 使用示例
# directory_path = 'E:\\Aphotos'  # 修改为你的目录路径
source_directory_path = 'D:\\34076\Pictures\Aphotos'  # 修改为你的目录路径
target_directory_path = 'D:\\34076\Pictures\Aphotos'  # 修改为你的目录路径
# convert_webp_to_png(source_directory_path, target_directory_path)
rename_files(source_directory_path)
