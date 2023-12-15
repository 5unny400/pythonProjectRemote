"""
@FileName：json_loads_dumps.py
@Description：
@Author：shenxinyuan
@Time：2023/12/14
"""
import json

# 原始数据，已经是 JSON 格式
original_data = {'key': 'value'}

# 第一次 JSON 编码
first_encode = json.dumps(original_data)
print(first_encode)
# 第二次 JSON 编码  就改变了 json 本来的样子
nested_json_string = json.dumps(first_encode)

print(nested_json_string)


json_loads = json.loads(nested_json_string)
print(json_loads)
json_loads2 = json.loads(json_loads)
print(json_loads2)
