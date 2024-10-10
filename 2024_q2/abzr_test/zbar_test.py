from PIL import Image
from pyzbar.pyzbar import decode

# 打开图像文件
image = Image.open('qrcode_test.png')

# 解码图像中的二维码
decoded_objects = decode(image)

# 打印解码结果
for obj in decoded_objects:
    print("Type:", obj.type)
    print("Data:", obj.data.decode("utf-8"))
