from datasketch import MinHash, MinHashLSHForest
import re

# 文本段落示例
texts = [
    "Python is a popular programming language.",
    "Java is another popular programming language.",
    "Python and Java are both programming languages."
]

# 定义一个函数来生成 MinHash 对象
def get_minhash(text):
    tokens = re.findall(r'\w+', text.lower())  # 将文本转换为小写并提取单词
    minhash = MinHash()
    for token in tokens:
        minhash.update(token.encode('utf8'))
    return minhash

# 创建 MinHashLSHForest 对象
forest = MinHashLSHForest(num_perm=128)

# 保存文本内容的列表
text_contents = []

# 为每个文本段落创建 MinHash 对象并添加到 forest 中
for text in texts:
    minhash = get_minhash(text)
    forest.add(len(text_contents), minhash)  # 使用列表索引作为键
    text_contents.append(text)  # 保存文本内容

# 构建索引
forest.index()

# 查询与 text1 相似的文本段落
query = get_minhash(texts[0])
threshold = 0.5  # 设定相似度阈值
result = forest.query(query, 3)  # 查询与 text1 最相似的 3 个文本段落

for index in result:
    if index != 0:  # 排除查询对象本身
        text = text_contents[index]
        minhash = get_minhash(text)
        similarity = query.jaccard(minhash)  # 计算 Jaccard 相似度
        if similarity >= threshold:
            print(f"Text: {text}, Similarity: {similarity}")
