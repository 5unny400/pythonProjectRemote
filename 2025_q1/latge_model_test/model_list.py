"""
@FileName：model_list
@Description：
@Author：shenxinyuan
@Time：2025/2/7
"""
from openai import OpenAI
from key import DeepSeek_API_KEY

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key=DeepSeek_API_KEY, base_url="https://api.deepseek.com")
print(client.models.list())
