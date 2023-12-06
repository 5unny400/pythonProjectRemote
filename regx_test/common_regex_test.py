"""
@FileName：common_regex_test.py
@Description：
@Author：shenxinyuan
@Time：2023/12/5
"""
import re

# 匹配中文 数字 英文大小写 下划线 %  还有 ——  - 空格
# re_check_task_name = "[\\u4e00-\\u9fef0-9a-zA-Z\\_\\-\\—\\ \\%]"

# 匹配中文 数字 英文大小写 下划线 %
# re_check_task_name = "[\u4e00-\u9fef0-9a-zA-Z_%]"

# 半角和全角
re_check_task_name = "[\u3001\u4e00-\u9fef0-9a-zA-Z_ -——‘’“”'\"！!？?*%#【】；（）()…….。，,]"

name = "中文Aa33——_- 22%%%% 连接号- 破折号—— 省略号...。。。 单引号‘’'' 双引号“” "" 感叹号！! ?？*%#{}[]【】；;@&()（）…….......、,，"
# name = str("测试String123!@#$%^&*()_+中文abcXYZ&#8203;``【oaicite:2】``&#8203;{}[]|\:;"'<>,.?/~`'"")
# name = str("!@#$%^&*()_+Lorem Ipsum 12345abcXYZ&#8203;``【oaicite:1】``&#8203;{}[]|\:;"'<>,.?/~`'"")
# name = str("12345abcXYZ&#8203;``【oaicite:0】``&#8203;{}[]|\:;\"'<>,.?/~`\'Lorem Ipsum!@#$%^&*()_+")
matches = re.findall(re_check_task_name, name)

res = len(matches) == len(name)

print(name)
print("".join(matches))
print(res)
