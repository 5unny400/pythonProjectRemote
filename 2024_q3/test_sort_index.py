rule_list = [
    {'rule_id': 1, 'sort_index': 3},
    {'rule_id': 2, 'sort_index': None},
    {'rule_id': 3, 'sort_index': 1},
    {'rule_id': 4, 'sort_index': 2},
    {'rule_id': 5, 'sort_index': None}
]
rule_list.sort(key=lambda x: x['sort_index'] if x['sort_index'] is not None else 1000)


print(rule_list)

# 可以看到，sort_index 为 None 的元素被排在了最后，因为它们的排序关键字为 1000，而其他元素按照其 sort_index 属性进行了排序。
# 这个例子展示了 1000 的使用，它确保了那些没有明确排序索引的元素被排在后面

