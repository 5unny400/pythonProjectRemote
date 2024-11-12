"""
@FileName：lambda_test_4
@Description：
@Author：shenxinyuan
@Time：2024/10/29
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # 输出:[2,4,6,8]
