"""
@FileName：test_k8s.py
@Description：
@Author：shenxinyuan
@Time：2024/5/7
"""
# -*- coding: utf-8 -*-
input_str = """
      - ../../../../globally_share_data/api_upload_data:/extract_share_data
      - ../../../../globally_share_data/extract_data/rule_extract/data:/data/data
      - ../../../../globally_share_data/global_conf:/data/global_conf:ro
"""
tmeplate = """
        - name: mount-data
          mountPath: {}
          subPath: {}
"""
tmeplate = tmeplate.replace('\n', '', 1)


def pre_process(input_item: str):
    """
    预处理
    """
    return input_item.replace('- ../../../../', '').strip()


if __name__ == '__main__':
    input_list = input_str.strip().split('\n')
    for item in input_list:
        item = pre_process(item)
        subPath, mountPath = item.split(':')
        print(tmeplate.format(mountPath, subPath).rstrip())

