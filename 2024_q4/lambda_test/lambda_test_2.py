"""
@FileName：lambda_test_2
@Description：
@Author：shenxinyuan
@Time：2024/10/29
"""
#有一个包含元组的列表，元组中有名字和年龄
people=[("Alice",30),("Bob",25),("Charlie",35)]

#使用lambda按年龄排序
sorted_by_age=sorted(people,key=lambda person:person[1])

print(sorted_by_age)
