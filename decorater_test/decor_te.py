import time
from functools import wraps


# 测试装饰器  被该装饰器修饰的函数都会打印函数运行时间日志
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        # execution_time = end_time - start_time
        print(f"函数 {func.__name__} 执行时间为: {end_time - start_time} 秒")
        return result

    return wrapper


# def transaction_client(func):
#     @wraps(func)
#     def wrapper(*args, **kw):
#         try:
#             res = func(*args, **kw)
#             session.flush()
#             session.commit()
#             return res
#         except Exception as e:
#             logger.exception(e)
#             session.rollback()
#             raise ClientError(message=str(e))
#
#     return wrapper


@timer
def my_function():
    time.sleep(2)
    print("函数执行完成")


my_function()
