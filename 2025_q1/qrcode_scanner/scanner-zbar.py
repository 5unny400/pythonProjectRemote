"""
@FileName：scanner-zbar
@Description：
@Author：shenxinyuan
@Time：2025/2/10
"""
import zbar
from PIL import Image

def get_barcode_with_zbar(img_path):
    # 打开图像文件
    image = Image.open(img_path).convert('L')  # 转换为灰度图像
    width, height = image.size
    raw = image.tobytes()

    # 创建扫描器
    scanner = zbar.ImageScanner()
    scanner.parse_config('enable')

    # 创建 zbar 图像
    zbar_image = zbar.Image(width, height, 'Y800', raw)

    # 扫描图像
    scanner.scan(zbar_image)

    # 获取结果
    for symbol in zbar_image:
        return symbol.data.decode('utf-8')

    return "Barcode Not Detected or your barcode is blank/corrupted!"

# 使用示例
barcode_data = get_barcode_with_zbar('./img.png')
print(barcode_data)