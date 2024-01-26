"""
@FileName：check-permission_deco_test.py
@Description：
@Author：shenxinyuan
@Time：2024/1/23
"""
from functools import wraps

def check_task_permission(func):
    @wraps(func)
    def wrapper(task_id, user=None, *args, **kwargs):
        """
        校验用户是否有任务资源权限 没有会抛异常
        """
        if not user:
            user = current_user

        creator_id = bank_flow_task_model.query_creator_id_by_task_id(task_id)
        if creator_id and (
            user.is_admin_permission()
            or creator_id == user.id
            or bank_flow_task_user_relation_model.query_by_user_id_and_task_id(task_id, user.id)
        ):
            return func(task_id, user, *args, **kwargs)
        else:
            EF.raise_message_exception("任务不存在或权限不足")

    return wrapper

# 使用装饰器
@check_task_permission
def some_protected_function(task_id, user):
    # 原始函数的逻辑
    pass
