"""
@FileName：python-pyzxing
@Description：
@Author：shenxinyuan
@Time：2025/2/10
"""
from pyzxing import BarCodeReader


def scan_barcode_qr_code(image_path):
    reader = BarCodeReader()
    results = reader.decode(image_path)

    if not results:
        print("未检测到条形码或二维码")
        return None

    for result in results:
        barcode_format = result['format']
        barcode_data = result['parsed']
        print(f"条码类型: {barcode_format}")
        print(f"条码内容: {barcode_data}")
        if str(barcode_data.decode('utf-8')).startswith("SF"):
            print(f"顺丰运单号：{str(barcode_data.decode('utf-8'))}")

    return results


# 示例用法
image_path = "img.png"  # 替换为你的图像路径
scan_barcode_qr_code(image_path)