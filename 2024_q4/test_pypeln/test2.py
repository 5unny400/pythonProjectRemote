"""
@FileName：test2
@Description：本样例不会出现任务丢失的问题
@Author：shenxinyuan
@Time：2024/12/30
"""
import asyncio
import time

import unittest

# 限制并发数量
semaphore = asyncio.Semaphore(10)
batch_size = 40


class ConCheckTest(unittest.TestCase):

    async def get_gis_info2(self, address: str):
        # async with semaphore:
        #     await asyncio.sleep(0.5)  # 使用异步睡眠
        await asyncio.sleep(0.5)  # 使用异步睡眠
        return address

    async def run_tests(self):
        fhj_send_address_list = [str(x) for x in range(78)]
        for x in range(99):
            print(f"第{x + 1}次测试")
            start_time = time.time()
            print(f"len(fhj_send_address_list)={len(fhj_send_address_list)}")
            res_count = 0
            for i in range(0, len(fhj_send_address_list), batch_size):
                batch = fhj_send_address_list[i:i + batch_size]
                tasks = [self.get_gis_info2(address) for address in batch]
                gis_ctx_send = await asyncio.gather(*tasks, return_exceptions=True)
                # 处理错误
                for result in gis_ctx_send:
                    if isinstance(result, Exception):
                        print(f"任务出错: {result}")
                print(f"len(gis_ctx_send)={len(gis_ctx_send)}")
                res_count += len(gis_ctx_send)
            print(f"res_count={res_count}")
            end_time = time.time()
            print(f"耗时={end_time - start_time}s")

    def test_pypeln_task(self):
        asyncio.run(self.run_tests())  # 在测试方法中运行异步任务
