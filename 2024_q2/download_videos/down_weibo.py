"""
@FileName：down_weibo.py
@Description：
@Author：shenxinyuan
@Time：2024/4/3
"""
import re
import requests


def download_weibo_video(weibo_url):
    # 发送请求获取微博页面的HTML内容
    response = requests.get(weibo_url)
    html_content = response.text

    # 使用正则表达式提取视频链接
    video_url_match = re.search(r'"video_url":"(https://[^"]+)"', html_content)
    if video_url_match:
        video_url = video_url_match.group(1)
        # 下载视频
        response = requests.get(video_url)
        with open("downloaded_video.mp4", "wb") as f:
            f.write(response.content)
        print("Video downloaded successfully!")
    else:
        print("Failed to extract video URL from the Weibo page.")


# 输入微博链接
weibo_url = input("Enter the Weibo video URL: ")

# 下载视频
download_weibo_video(weibo_url)
