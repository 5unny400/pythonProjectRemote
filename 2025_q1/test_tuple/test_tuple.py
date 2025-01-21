"""
@FileName：test_tuple
@Description：
@Author：shenxinyuan
@Time：2025/1/17
"""
a = ()
print(type(a))

b = (1)
print(type(b))

c = [2]
print(type(c))

d = (3,)
print(type(d))

e = (4, 5, 6)
print(type(e))

# <class 'tuple'>
# <class 'int'>
# <class 'list'>
# <class 'tuple'>
# <class 'tuple'>


res = ord('A')
print(res)
# 65

res = ord('中')
print(res)
# 20013

res = chr(66)
# 'B'
print(res)

res = chr(25991)
# '文'
print(res)


s = 'ABC'.encode('ascii')
print(s)

s = b'ABC'
print(s)

s = '中文'.encode('utf-8')
print(s)

s = b'\xe4\xb8\xad\xe6\x96\x87'
print(s)
# s = '中文'.encode('ascii')   # 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错
# print(s)
