# 互联网下载器
# 首先安装internetdownloadmanager库
# pip install internetdownloadmanager
import internetdownloadmanager as idm


def downloader(urls, output):
    pydownloader = idm.Downloader(worker=20,
                                  part_size=1024 * 1024 * 10,
                                  resumable=True, )
    index = 0
    for url in urls:
        pydownloader.download(url, f"{output}-{index}.jpg")


to_download_pic_address_list = ["https://i-blog.csdnimg.cn/blog_migrate/66ecc94d7f169baa0b13f132ba61ddbd.png#pic_center"]

downloader(to_download_pic_address_list, "")
