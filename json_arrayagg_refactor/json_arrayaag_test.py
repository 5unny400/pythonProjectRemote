"""
@FileName：json_arrayaag_test.py
@Description：
@Author：shenxinyuan
@Time：2023/12/4
"""
# SELECT
#   department,
#   GROUP_CONCAT(employee_name) AS employees
# FROM
#   employees
# GROUP BY
#   department;
#
# | department | employees      |
# |------------|----------------|
# | HR         | Alice,Bob      |
# | IT         | Charlie,David  |

import json

# 假设 rows 是从数据库获取的查询结果
rows = [("HR", "Alice"), ("HR", "Bob"), ("IT", "Charlie"), ("IT", "David")]

result_dict = {}
for row in rows:
    department, employee_name = row
    if department not in result_dict:
        result_dict[department] = []
    result_dict[department].append(employee_name)

result_json = json.dumps(result_dict)
print(result_json)
