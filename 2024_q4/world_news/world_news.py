"""
@FileName：world_news 还可以对接更多的接口和不同的入参
@Description：
@Author：shenxinyuan
@Time：2024/11/21
"""
import json

# 获取世界新闻 https://worldnewsapi.com/console/#    https://worldnewsapi.com/docs/search-news/
# 首先安装requests库
# pip install requests
import requests

ApiKey = "0b25442203a04aa8b7df3d7dcb181a11"
url = f"https://api.worldnewsapi.com/search-news?text=hurricane&api-key={ApiKey}"
# url = f"https://api.worldnewsapi.com/top-news?text=hurricane&api-key={ApiKey}"
headers = {
    'Accept': 'application/json'
}
response = requests.get(url, headers=headers)
res = json.dumps(response.json(), indent=1)
print("News:", res)

with open('hurricane_news.txt', 'w', encoding='utf-8') as f:
    f.write(f"{res}\n")
    # for new in res.get('news'):
        # f.write(f"标题: {new['title']}\n")
        # f.write(f"发布时间: {new['publish_date']}\n")
        # f.write(f"摘要: {new['summary']}\n")
        # f.write(f"链接: {new['url']}\n")
        # f.write("\n---\n\n")
