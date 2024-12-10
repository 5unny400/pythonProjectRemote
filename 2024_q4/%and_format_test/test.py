"""
@FileName：test
@Description：
### 总结

- `%`是一种较老的字符串格式化方式，简单易用，但功能有限。
- `format`是现代的字符串格式化方法，功能更强大、灵活且可读性更高。
- 在 Python 3.6 及更高版本中，尤其是引入了 f-string（格式化字符串字面量）后，`format`方法常被用得较少，f-string 方式被广泛推崇。
@Author：shenxinyuan
@Time：2024/12/9
"""

name = "Alice"
age = 30
value = 123.456

# 使用 '%' 操作符
result_1 = "Name: %s, Age: %d, Value: %.2f" % (name, age, value)

# 使用 'str.format()' 方法
result_2 = "Name: {}, Age: {}, Value: {:.2f}".format(name, age, value)

# 使用 f-string
result_3 = f"Name: {name}, Age: {age}, Value: {value:.2f}"

print(result_1)  # Output: Name: Alice, Age: 30, Value: 123.46
print(result_2)  # Output: Name: Alice, Age: 30, Value: 123.46
print(result_3)  # Output: Name: Alice, Age: 30, Value: 123.46
# 注意：f-string 方式在 Python 3.6 及更高版本中才被支持，低版本的 Python 则需要使用 `format` 方法。
