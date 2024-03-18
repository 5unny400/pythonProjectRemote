"""
@FileName：aes_test.py
@Description：
@Author：shenxinyuan
@Time：2024/3/12
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project :
# @File    : aes_utils.py
# @Author  : wuyun@datagrand.com
# @Time    : 2022/7/20 11:52 上午
# @desc:
import base64
from urllib import parse

from Crypto.Cipher import AES

# from web_api.app.module_config.fund_contract_config import fund_contract_config


# from Cryptodome.Cipher import AES


class AESECBUtils(object):
    def __init__(self):
        self.key = "superadminpro"  # noqa 最好不要有标点符号
        self.MODE = AES.MODE_ECB
        self.length = AES.block_size
        self.cypher = AES.new(self.add_to_16(self.key), self.MODE)

    @staticmethod
    def add_to_16(raw_text):
        """
        str不是16的倍数那就补足为16的倍数
        """
        while len(raw_text) % 16 != 0:
            raw_text += " "
        return str.encode(raw_text)

    def encrypt(self, plaintext):
        """
        加密函数
        """
        if not isinstance(plaintext, str):
            plaintext = str(plaintext)
        encrypted_text = self.cypher.encrypt(self.add_to_16(plaintext))
        encrypted_text = str(base64.b64encode(encrypted_text), encoding="utf-8")
        return parse.quote(encrypted_text, safe="")

    def decrypt(self, ciphertext):
        """
        解密函数
        """
        ciphertext = parse.unquote(ciphertext)
        decode_text = base64.decodebytes(ciphertext.encode(encoding="utf-8"))
        decrypted_text = str(self.cypher.decrypt(decode_text), encoding="utf-8").replace(" ", "")
        return decrypted_text

    # def encrypt_by_config(self, plaintext):
    #     """
    #     根据配置加密
    #     """
    #     if fund_contract_config.enable_id_encrypt:
    #         return self.encrypt(plaintext)
    #     else:
    #         return plaintext
    #
    # def decrypt_by_config(self, ciphertext):
    #     """
    #     根据配置解密
    #     """
    #     if fund_contract_config.enable_id_encrypt:
    #         return self.decrypt(ciphertext)
    #     else:
    #         return ciphertext


aes_utils = AESECBUtils()

if __name__ == "__main__":
    # text = aes_utils.decrypt("dDGqmvlFk%2F5VdFJfUobEfg%3D%3D")
    text = aes_utils.decrypt("Z00mzDaOWmozzvtqUHv8Ng==")
    print(text)
