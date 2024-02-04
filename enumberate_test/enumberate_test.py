"""
@FileName：enumberate_test.py
@Description：
@Author：shenxinyuan
@Time：2023/12/6
"""
# 例子
my_list = ['apple', 'banana', 'orange']

my_tuple = 'apple', 'banana', 'orange'

print(type(my_list))
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

print(type(my_tuple))
for index, value in enumerate(my_tuple[1]):
    print(f"Index: {index}, Value: {value}")

# 输出:
# Index: 0, Value: apple
# Index: 1, Value: banana
# Index: 2, Value: orange


