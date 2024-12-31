"""
@FileName：test2
@Description：
@Author：shenxinyuan
@Time：2024/12/30
"""
import asyncio
import time

import pypeln
import unittest

class ConCheckTest(unittest.TestCase):
    async def get_gis_info2(self, address: str):
        # await asyncio.sleep(0.5)  # 使用异步睡眠
        time.sleep(0.5)  # 使用异步睡眠
        return address

    async def run_tests(self):
        fhj_send_address_list = [str(x) for x in range(78)]
        for x in range(3):
            print(f"第{x + 1}次测试")
            start_time = time.time()
            print(f"len(fhj_send_address_list)={len(fhj_send_address_list)}")
            tasks = [self.get_gis_info2(address) for address in fhj_send_address_list]
            gis_ctx_send = await asyncio.gather(*tasks, return_exceptions=True)  # 捕获异常
            # 处理错误
            for result in gis_ctx_send:
                if isinstance(result, Exception):
                    print(f"任务出错: {result}")
            print(f"len(gis_ctx_send)={len(gis_ctx_send)}")
            end_time = time.time()
            print(f"耗时={end_time - start_time}s")

    def test_pypeln_task(self):
        asyncio.run(self.run_tests())  # 在测试方法中运行异步任务
