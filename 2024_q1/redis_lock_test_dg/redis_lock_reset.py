"""
@FileName：redis_lock_reset.py
@Description：
@Author：shenxinyuan
@Time：2024/1/16
"""
# def reset_lock(lock_name: str):
#     """
#     重置redis锁
#     """    global _file_redis_connect
#     lock = None
#     try:
#         logger.info("reset_lock: {}".format(lock_name))
#         lock = redis_lock.Lock(_file_redis_connect, lock_name)
#         lock.reset()
#     except Exception as e:
#         logger.exception(e)
#         _file_redis_connect = get_redis_client(RedisConfig.redis_url)
#         # if lock:
#         #     lock.reset()
#     finally:
#         if lock:
#             lock.reset()