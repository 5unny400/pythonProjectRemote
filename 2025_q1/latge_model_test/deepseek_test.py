"""
@FileName：deepseek_test
@Description：
@Author：shenxinyuan
@Time：2025/2/7
"""
import time

# Please install OpenAI SDK first: `pip3 install openai`

from key import DeepSeek_API_KEY, deepseek_model
from openai import OpenAI

client = OpenAI(api_key=DeepSeek_API_KEY, base_url="https://api.deepseek.com")

# 初始化系统消息
system_content = "你是一个乐于助人的助手"

# 初始化对话消息列表
messages = [
    {"role": "system", "content": system_content},
]

print("exit: 退出对话\nchange system: 修改系统角色")

# 循环对话
while True:
    # 用户输入
    user_input = input("你: ")

    # 如果用户输入 'exit'，则退出循环
    if user_input.lower() == 'exit':
        print("助手: 好的，再见！")
        break

    # 如果用户输入 'change system'，则允许修改系统消息
    if user_input.lower() == 'change system':
        new_system_content = input("请输入新的系统角色内容: ")
        system_content = new_system_content
        # 更新系统消息
        messages[0]["content"] = system_content
        print(f"系统消息已更新为: {system_content}")
        continue

    # 将用户输入添加到对话消息列表中
    messages.append({"role": "user", "content": user_input})

    response = None
    # 获取助手的回复
    try:
        time_start = time.time()
        response = client.chat.completions.create(
            model=deepseek_model,
            messages=messages,
            stream=False
        )
        time_end = time.time()
        print(f"cost time: {time_end-time_start} s")
    except Exception as e:
        print(e)
    # 打印助手的回复
    assistant_reply = response.choices[0].message.content
    print(f"助手: {assistant_reply}")

    # 将助手的回复也添加到对话消息列表中
    messages.append({"role": "assistant", "content": assistant_reply})
