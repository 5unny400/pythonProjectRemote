from PIL import Image
import os


def convert_webp_to_png(directory):
    for filename in os.listdir(directory):
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
                # 删除原始的 WebP 格式图片
                os.remove(webp_file)
            except Exception as e:
                print(f"Error converting {webp_file}: {e}")


# 使用示例
directory_path = 'D:\\Administrator\\图片'  # 修改为你的目录路径
convert_webp_to_png(directory_path)
