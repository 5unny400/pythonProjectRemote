from PIL import Image  # 导入 Image
import barcode
from barcode.writer import ImageWriter

def get_barcode_with_python_barcode(img_path):
    # 打开图像文件
    image = Image.open(img_path).convert('L')  # 转换为灰度图像

    # 使用 python-barcode 识别条形码
    reader = barcode.get_barcode_reader()
    result = reader.decode(image)

    if result:
        return result
    else:
        return "Barcode Not Detected or your barcode is blank/corrupted!"

# 使用示例
barcode_data = get_barcode_with_python_barcode('img.png')
print(barcode_data)