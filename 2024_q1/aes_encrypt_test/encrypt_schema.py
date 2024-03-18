"""
@FileName：encrypt_schema.py
@Description：
@Author：shenxinyuan
@Time：2024/3/12
"""
import typing

from marshmallow import pre_load, post_dump, Schema
from marshmallow.utils import _Missing
from aes_test import aes_utils

class EncryptSchema(Schema):
    # 需要加解密的字段
    encrypt_field_list: typing.List[str] = []

    @pre_load
    def decrypt(self, data, **kwargs):  # noqa
        """
        解密操作可以在这处理
        """
        # if not ENABLE_ID_ENCRYPT:
        #     return data
        # data是代理Dict不可变所以需要重新构造一个
        try:
            res = {k: v for k, v in data.items()}
            for field in self.encrypt_field_list:
                input_data = data.get(field)
                if input_data is not None and not isinstance(input_data, _Missing):
                    if isinstance(input_data, list):
                        tmp_list = []
                        for item in input_data:
                            tmp_list.append(aes_utils.decrypt(item))
                        res[field] = tmp_list
                    else:
                        res[field] = aes_utils.decrypt(input_data)
        except Exception as e:
            # logger.exception(e)
            # raise MessageException("参数不正确")
            raise Exception("参数不正确{}".format(e))
        return res

    @post_dump
    def encrypt(self, data, **kwargs):  # noqa
        """
        加密操作可以在这处理
        """
        # if not ENABLE_ID_ENCRYPT:
        #     return data
        for field in self.encrypt_field_list:
            input_data = data.get(field)
            if input_data is not None:
                if isinstance(input_data, list):
                    tmp_list = []
                    for item in input_data:
                        tmp_list.append(aes_utils.encrypt(item))
                    data[field] = tmp_list
                else:
                    data[field] = aes_utils.encrypt(input_data)
        return data


class TaskAndFileIdSchema(EncryptSchema):
    encrypt_field_list = ["task_id", "file_id"]
