"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2025/1/21
"""
print(sorted([36, 5, -12, 9, -21]))
# [-21, -12, 5, 9, 36]

print(sorted([36, 5, -12, 9, -21], key=abs))
# [5, 9, -12, -21, 36]

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# ['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
# ['Zoo', 'Credit', 'bob', 'about']


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L1 = sorted(L, key=by_name)
print(L1)
def by_score(t):
    return t[1]

L2 = sorted(L, key=by_score,reverse=True)
print(L2)