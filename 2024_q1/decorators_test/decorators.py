"""
@FileName：decorators.py
@Description：
@Author：shenxinyuan
@Time：2024/3/20
"""
from functools import wraps

from flask import request


def get_nested_value(data, key):
    """
    递归函数，从嵌套的字典中获取值
    """
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                return v
            elif isinstance(v, (dict, list)):
                result = get_nested_value(v, key)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for item in data:
            result = get_nested_value(item, key)
            if result is not None:
                return result
    return None


def add_task_id(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        task_id = request.headers.get('task_id')
        if not task_id:
            task_id = request.args.get('task_id')  # 从请求参数中获取
        if not task_id:
            task_id = get_nested_value(request.json, 'task_id')  # 从请求体中获取
        if not task_id:
            # 如果task_id不存在于任何地方，则可以根据具体情况进行处理，可能需要抛出异常或者使用默认值
            pass
        # BankFlowShardingManager.create_sharding_manager(task_id)
        return func(*args, **kwargs)

    return wrapper


class _BaseResourceWithoutAuth(Resource):
    """继承Resource
    不含权限验证
    """

    method_decorators = dict(
        head=[add_task_id],
        get=[add_task_id],
        post=[add_task_id],
        put=[add_task_id],
        delete=[add_task_id],
        patch=[add_task_id],
    )

# 注解add_task_id获取到的 task_id 已经是解密后的：
# 是的，如果`@pre_load`注解修饰的`decrypt_task_id`方法成功解密了`task_id`并将解密后的值存储在`BaseSchema`实例的属性中，
# 那么在`add_task_id`装饰器中直接获取这个属性就是解密后的`task_id`。因此，你在`add_task_id`装饰器中获取到的`task_id`已经是解密后的值了。


# 但是实际测试却是 request.get先拿到了没有解密的 task_id。因此 在baseresource添加这个注解还是不太可行。
