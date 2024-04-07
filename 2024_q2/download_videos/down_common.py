"""
@FileName：down_common.py
@Description：
@Author：shenxinyuan
@Time：2024/4/3
"""
import youtube_dl

def download_video(video_url):
    ydl_opts = {
        'outtmpl': 'downloaded_video.mp4',  # 保存文件名
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

# 输入视频链接
video_url = input("Enter the video URL: ")

# 下载视频
download_video(video_url)
