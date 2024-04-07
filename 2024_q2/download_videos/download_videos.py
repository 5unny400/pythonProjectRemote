"""
@FileName：download_videos.py
@Description：
@Author：shenxinyuan
@Time：2024/4/3
"""
from pytube import YouTube

# 视频链接
video_url = "https://www.youtube.com/watch?v=VIDEO_ID"

# 创建YouTube对象
yt = YouTube(video_url)

# 获取视频流
stream = yt.streams.get_highest_resolution()

# 下载视频到当前目录
stream.download()
