"""
@FileName：asymmetric_encryption_test.py
@Description：
@Author：shenxinyuan
@Time：2024/2/22
"""
import string

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# 生成RSA密钥对
key = RSA.generate(2048)

# 获取公钥和私钥
public_key = key.publickey().export_key()
private_key = key.export_key()

print("public_key:" + public_key)
print("private_key:" + private_key) 

# 明文
plain_text = b"Hello, this is a message to be encrypted using asymmetric encryption."

# 加密
cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
encrypted_bytes = cipher.encrypt(plain_text)

# 解密
cipher = PKCS1_OAEP.new(RSA.import_key(private_key))
decrypted_bytes = cipher.decrypt(encrypted_bytes)

# 输出加密后的结果和解密后的结果
print("加密后：" + base64.b64encode(encrypted_bytes).decode())
print("解密后：" + decrypted_bytes.decode())
