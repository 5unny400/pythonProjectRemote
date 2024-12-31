"""
@FileName：test_run
@Description：   本代码样例也会有任务丢失的问题，最严重
@Author：shenxinyuan
@Time：2024/12/31
"""
import unittest
import time
import asyncio
import pypeln


class ConCheckTest(unittest.TestCase):
    # 异步任务函数
    async def get_gis_info2(self, address: str):
        await asyncio.sleep(0.5)  # 模拟异步延时
        return address

    # 异步执行的测试函数
    def test_pypeln_task(self):
        fhj_send_address_list = [str(x) for x in range(78)]  # 测试地址列表

        # 测试执行多次
        for x in range(99):
            print(f"第{x + 1}次测试")
            start_time = time.time()
            print(f"len(fhj_send_address_list)={len(fhj_send_address_list)}")

            # 使用 asyncio.run() 来执行异步任务
            gis_ctx_send = asyncio.run(self.run_pypeln_task(fhj_send_address_list))

            print(f"len(gis_ctx_send)={len(gis_ctx_send)}")
            end_time = time.time()
            print(f"耗时={end_time - start_time}s")

    # 用 async 包装 pypeln.task.map 的调用
    async def run_pypeln_task(self, fhj_send_address_list):
        # 执行异步任务，使用 pypeln.task.map
        return await pypeln.task.map(self.get_gis_info2, fhj_send_address_list, workers=5, maxsize=5)


# 如果你希望直接运行单元测试，请取消以下两行的注释
if __name__ == '__main__':
    unittest.main()



# 第1次测试
# len(fhj_send_address_list)=78
# len(gis_ctx_send)=78
# 耗时=8.02998399734497s
# 第2次测试
# len(fhj_send_address_list)=78
# len(gis_ctx_send)=78
# 耗时=8.0398268699646s
# 第3次测试
# len(fhj_send_address_list)=78
# len(gis_ctx_send)=9
# 耗时=1.0134100914001465s
# 第4次测试
# len(fhj_send_address_list)=78
# len(gis_ctx_send)=78
# 耗时=8.03721809387207s
# 第5次测试
# len(fhj_send_address_list)=78
# len(gis_ctx_send)=78
# 耗时=8.045849800109863s
# 第6次测试
# len(fhj_send_address_list)=78
# len(gis_ctx_send)=78
# 耗时=8.034311056137085s
# 第7次测试
# len(fhj_send_address_list)=78
# len(gis_ctx_send)=76
# 耗时=8.03787899017334s

