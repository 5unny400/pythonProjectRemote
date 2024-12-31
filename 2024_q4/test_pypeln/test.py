"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2024/12/30
"""
import asyncio
import time
import unittest
import pypeln


class ConCheckTest(unittest.TestCase):
    # async def task_process(self, address: str):
    #     await asyncio.sleep(0.5)
    #     return address

    async def get_gis_info2(self, address: str):
        await asyncio.sleep(0.5)
        # time.sleep(0.5)
        return address

    def test_pypeln_task(self):
        fhj_send_address_list = [str(x) for x in range(78)]
        for x in range(99):
            print(f"第{x + 1}次测试")
            start_time = time.time()
            print(f"len(fhj_send_address_list)={len(fhj_send_address_list)}")
            gis_ctx_send = list(pypeln.task.map(self.get_gis_info2, fhj_send_address_list, workers=5, maxsize=5))
            print(f"len(gis_ctx_send)={len(gis_ctx_send)}")
            end_time = time.time()
            print(f"耗时={end_time - start_time}s")


# 问题： 同步或者异步的 sleep 都会导致gis_ctx_send的长度有概率小于fhj_send_address_list的长度？
# 增大 maxsize 的值，似乎可以解决偶尔会有任务丢失的问题。
