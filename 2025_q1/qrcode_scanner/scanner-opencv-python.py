import json
import os
import cv2
import time


def get_image_files(directory, extensions=('.jpg', '.jpeg', '.png')):
    """
    遍历指定目录及其子目录，获取所有图片文件的名称。
    :param directory: 要遍历的目录路径
    :param extensions: 支持的图片文件扩展名列表
    :return: 包含所有图片文件名称的列表
    """
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                image_files.append(os.path.join(root, file))
    return image_files


def get_barcode(img, resize=4):
    image = cv2.imread(img)
    new_image = cv2.resize(image, (image.shape[1] * resize, image.shape[0] * resize), interpolation=cv2.INTER_CUBIC)

    # 使用 OpenCV 的 QRCodeDetector 来检测和解码 QR 码
    qr_detector = cv2.QRCodeDetector()
    qr_data, qr_bbox, qr_points = qr_detector.detectAndDecode(new_image)

    # 使用 OpenCV 的 barcode_BarcodeDetector 来检测和解码条形码（这里识别不到条码内容？）
    barcode_detector = cv2.barcode.BarcodeDetector()
    barcode_data, barcode_bbox, barcode_points = barcode_detector.detectAndDecode(new_image)

    if qr_data == "" and barcode_points is None:
        barcode_data = "Barcode Not Detected or your barcode is blank/corrupted!"
    else:
        if barcode_points is not None:
            barcode_data = barcode_data[0]
            print("条形码结果")
        else:
            barcode_data = qr_data
            print("二维码结果")
            qr_data_dict = json.loads(qr_data.replace("'", '"').split("=")[1])
            sf_no = qr_data_dict.get("k5")
            print(f"顺丰快递单号：{sf_no}")

    return barcode_data


def batch_test():
    pics = get_image_files(".")
    for pic in pics:
        barcode = get_barcode(pic)
        print("{}: {}".format(pic, barcode))


def unit_test(pic_path):
    barcode = get_barcode(pic_path)
    print("{}: {}".format(pic_path, barcode))


if __name__ == '__main__':
    start_time = time.time()
    unit_test("./img2.png")
    # batch_test()
    end_time = time.time()
    print(f"条形码-二维码识别耗时{end_time-start_time}")
