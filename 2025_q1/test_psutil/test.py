"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2025/1/16
"""
import psutil

print(psutil.cpu_count())
#4
print(psutil.cpu_count(logical=False))
#2
# 2说明是双核超线程, 4则是4核非超线程

# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

def loop_cpu():
    for x in range(10):
        print(psutil.cpu_percent(interval=1, percpu=True))

loop_cpu()