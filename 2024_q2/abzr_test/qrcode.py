import qrcode

# 创建二维码对象
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# 设置二维码内容
data = "Hello, this is a QR code for testing!"
qr.add_data(data)
qr.make(fit=True)

# 生成图像
img = qr.make_image(fill='black', back_color='white')

# 保存二维码图像
img.save('qrcode_test.png')

print("QR code generated and saved as 'qrcode_test.png'")
