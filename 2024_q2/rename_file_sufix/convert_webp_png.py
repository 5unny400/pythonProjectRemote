from PIL import Image
import os


def convert_webp_to_png(directory):
    index = 1
    cnt = 0
    for filename in os.listdir(directory):
        cnt += 1
        if filename.endswith('.webp'):
            webp_file = os.path.join(directory, filename)
            png_file = os.path.join(directory, filename.replace('.webp', '.png'))
            try:
                # 打开 WebP 格式的图片
                with Image.open(webp_file) as img:
                    # 转换为 RGB 模式（避免包含 alpha 通道）
                    img = img.convert('RGB')
                    # 保存为 PNG 格式的图片
                    img.save(png_file, 'PNG')
                    print(str(index)+":"+png_file+"已修改为png格式！")
                # 删除原始的 WebP 格式图片
                os.remove(webp_file)
                index += 1
            except Exception as e:
                print(f"Error converting {webp_file}: {e}")
    print(f"一共遍历了{cnt}张图片。")


# 使用示例
directory_path = 'E:\\photos'  # 修改为你的目录路径
convert_webp_to_png(directory_path)
