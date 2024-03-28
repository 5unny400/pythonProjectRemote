"""
@FileName：shariding_decorator.py
@Description：
@Author：shenxinyuan
@Time：2024/3/22
"""
def sharding_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result_list = []
        result_dict = {}
        task_ids = kwargs.pop("task_ids")
        if not task_ids:
            task_ids = kwargs.get("task_id")
        task_id_dict = BankFlowShardingManager.grouping_task_id(task_ids)
        for k, group_task_ids in task_id_dict.items():
            if group_task_ids:
                BankFlowShardingManager.create_sharding_manager(group_task_ids[0])
                kwargs.update({"task_ids": group_task_ids})
                result = func(*args, **kwargs)
                if result:
                    if isinstance(result, dict):
                        result_dict.update(result)
                    elif isinstance(result, list):
                        result_list.extend(result)
                    else:
                        result_list.append(result)
                # result_list.extend(result)
        return result_dict if result_dict else result_list

    return wrapper