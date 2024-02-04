"""
@FileName：min_hash.py
@Description：
@Author：shenxinyuan
@Time：2024/1/16
"""
from datasketch import MinHash, MinHashLSH

# 创建两个集合
set1 = set(["apple", "orange", "banana", "kiwi"])
set2 = set(["apple", "pear", "banana", "grape"])

# 创建 MinHash 对象
minhash1 = MinHash()
minhash2 = MinHash()

# 添加元素到 MinHash
for word in set1:
    minhash1.update(word.encode('utf-8'))

for word in set2:
    minhash2.update(word.encode('utf-8'))

# 创建 MinHash LSH（Locality-Sensitive Hashing）索引
lsh = MinHashLSH(threshold=0.5, num_perm=128)
lsh.insert("set1", minhash1)
lsh.insert("set2", minhash2)

# 查询相似的集合
result = lsh.query(minhash1)
print("Approximate Jaccard Similarity:", minhash1.jaccard(minhash2))
print("Approximate Similar Sets:", result)
