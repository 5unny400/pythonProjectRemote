import time

import pypeln as pl
import asyncio
from random import random


async def slow_add1(x):
    await asyncio.sleep(0.05)  # <= some slow computation
    return x + 1


async def slow_gt3(x):
    await asyncio.sleep(random())  # <= some slow computation
    return x > 3

time_start = time.time()
data = range(69)  # [0, 1, 2, ..., 69]
stage = pl.task.map(slow_add1, data, workers=5, maxsize=10)
# stage = pl.task.filter(slow_gt3, stage, workers=2)
data = list(stage)  # e.g. [5, 6, 9, 4, 8, 10, 7]
data.sort()
time_end = time.time()
print(f"time_cost:{time_end - time_start} seconds")
print(f"data:{data} \n len(data):{len(data)}")
