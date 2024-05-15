from collections import defaultdict

# 假设数据存储在一个名为 data 的列表中，每个元素是一个字典，包含账号名（'username'）、账号（'account'）等字段
data = [
    {'username': 'user1', 'account': 'acc1', 'other_field': 'value1'},
    {'username': 'user2', 'account': 'acc2', 'other_field': 'value2'},
    {'username': 'user1', 'account': 'acc3', 'other_field': 'value3'},
    {'username': 'user3', 'account': 'acc2', 'other_field': 'value4'},
    {'username': 'user4', 'account': 'acc4', 'other_field': 'value5'},
    {'username': 'user5', 'account': 'acc5', 'other_field': 'value6'},
    {'username': 'user2', 'account': 'acc6', 'other_field': 'value7'},
    {'username': 'user1', 'account': 'acc7', 'other_field': 'value8'},
    {'username': 'user6', 'account': 'acc8', 'other_field': 'value9'},
    {'username': 'user3', 'account': 'acc9', 'other_field': 'value10'}
]


# 构建账号名到账号的映射字典
username_to_accounts = defaultdict(set)
for entry in data:
    username = entry['username']
    account = entry['account']
    username_to_accounts[username].add(account)

# 打上标记
marked_accounts = set()
for accounts in username_to_accounts.values():
    if len(accounts) > 1:
        marked_accounts.update(accounts)

# 分组数据
grouped_data = defaultdict(list)
for entry in data:
    username = entry['username']
    account = entry['account']
    if account in marked_accounts:
        grouped_data[username].append(entry)

# 打印分组数据
for username, entries in grouped_data.items():
    print(f"Group for username '{username}':")
    for entry in entries:
        print(entry)
    print()
