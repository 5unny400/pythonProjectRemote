#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Yang Huiyu
# @Date  : 2024/11/5

import os
import zxingcpp
from pyzbar import pyzbar
import cv2


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


def get_barcode(img, decode_mode="zxing", resize=4):
    image = cv2.imread(img)
    new_image = cv2.resize(image, (image.shape[1]*resize, image.shape[0]*resize), interpolation=cv2.INTER_CUBIC)
    if decode_mode == "zxing":
        barcodes = zxingcpp.read_barcodes(new_image)
        barcodes = [bc for bc in barcodes if "QR" not in bc.format.name]
    else:
        barcodes = pyzbar.decode(new_image)
        barcodes = [bc for bc in barcodes if bc.type != "QRCODE"]
    if barcodes == []:
        barcode_data = "Barcode Not Detected or your barcode is blank/corrupted!"
    else:
        if decode_mode == "zxing":
            barcode_data = barcodes[0].text
        else:
            barcode_data = barcodes[0].data.decode("utf-8")
    return barcode_data


def batch_test():
    pics = get_image_files("./data")
    for pic in pics:
        barcode = get_barcode(pic)
        print("{}: {}".format(pic, barcode))


def unit_test(pic_path):
    barcode = get_barcode(pic_path)
    print("{}: {}".format(pic_path, barcode))


if __name__ == '__main__':
    # unit_test("./data/2024-09-27 112410.jpg")
    unit_test("./img.png")
    # batch_test()

