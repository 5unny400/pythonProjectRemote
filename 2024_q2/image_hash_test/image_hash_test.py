"""
@FileName：image_hash_test.py
@Description： 哈希 相似度
@Author：shenxinyuan
@Time：2024/5/14
"""
from PIL import Image
import imagehash

# 加载图像
image1 = Image.open('image1.png')
image2 = Image.open('images2.png')

# 计算哈希值
hash1 = imagehash.average_hash(image1)
hash2 = imagehash.average_hash(image2)

# 比较哈希值
print("Hash 1:", hash1)
print("Hash 2:", hash2)
print("Hamming distance:", hash1 - hash2)
