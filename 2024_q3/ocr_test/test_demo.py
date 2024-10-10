from PIL import Image
import pytesseract


# 如果你使用Windows，你需要指定tesseract.exe的路径
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# macOS或Linux可能不需要手动指定路径，但如果需要，可以这样做：
# pytesseract.pytesseract.tesseract_cmd = '/Users/shenxinyuan/PycharmProjects/pythonProject/venv/lib/python3.11/site-packages/pytesseract/pytesseract.py'

# 打开图片
image_path = 'solid.jpg'
image = Image.open(image_path)

# 进行OCR识别
text = pytesseract.image_to_string(image, lang='eng')  # 'eng'表示使用英语语言包

print(text)
