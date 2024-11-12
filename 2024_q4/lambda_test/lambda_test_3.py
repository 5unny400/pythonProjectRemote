"""
@FileName：lambda_test2
@Description：
@Author：shenxinyuan
@Time：2024/10/29
"""
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # 输出:[1,4,9,16,25]

