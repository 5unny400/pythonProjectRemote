#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Yang Huiyu
# @Date  : 2024/11/5

import os
from zbarlight import scan_codes
from PIL import Image


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
    image = Image.open(img)
    image = image.resize((image.width * resize, image.height * resize), Image.BICUBIC)
    image = image.convert('L')  # Convert to grayscale

    # Scan for supported barcode types
    codes = scan_codes(['ean13', 'ean8', 'upc', 'isbn10', 'isbn13', 'code39', 'code128', 'code93'], image)

    if codes is None or len(codes) == 0:
        barcode_data = "Barcode Not Detected or your barcode is blank/corrupted!"
    else:
        barcode_data = codes[0].decode("utf-8")
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
    unit_test("./img.png")
    # batch_test()
