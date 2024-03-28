"""
@FileName：max_num.py
@Description：
@Author：shenxinyuan
@Time：2024/3/18
"""
import sys
from functools import wraps

from flask import request

print(sys.maxsize)


def validate_params():
    def wrapper(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            args_data = request.args.to_dict() if request.args is not None else {}
            form_data = request.form.to_dict() if request.form is not None else {}
            json_data = request.json if request.json is not None else {}

            all_args = {**args_data, **json_data, **form_data}
            # 定义一个最大值常量
            MAX_OFFSET_LIMIT = 1000_0000  # noqa
            # 定义需要校验的变量名列表
            VALIDATE_VARIABLES = ["start", "number", "offset", "limit"]  # noqa
            for var_name in VALIDATE_VARIABLES:
                # 从 kwargs 中获取变量的值
                value = all_args.get(var_name, None)
                if value is None:
                    continue
                elif isinstance(value, str):
                    try:
                        # 给value去除空格
                        value = int(value.strip())
                    except ValueError:
                        return Exception("")
                elif isinstance(value, int):
                    pass
                else:
                    return Exception()

                # 检查变量的值
                if value < 0:
                    return Exception()
                if value > MAX_OFFSET_LIMIT:
                    return Exception()

            return func(*args, **kwargs)

        return decorator

    return wrapper

# 如果在装饰器内部调用了被修饰的函数，并且返回了另一个变量，那么被修饰的原函数不会执行。被修饰的原函数只有在装饰器内部显式调用它时才会执行。
# 如果被修饰的原函数没有在装饰器内部显式调用，那么它就不会执行。
# 装饰器内部是否调用原函数决定了装饰器的执行时机。如果装饰器内部调用了原函数，装饰器会在原函数之前执行；如果装饰器内部没有调用原函数，装饰器会在原函数之后执行。
