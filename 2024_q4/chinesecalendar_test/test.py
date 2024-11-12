"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2024/11/12
"""
import datetime

# 判断 2018年4月30号 是不是节假日
from chinese_calendar import is_holiday, is_workday

april_last = datetime.date(2022, 3, 23)
print('is_holiday: ', is_holiday(april_last))
print('is_workday: ', is_workday(april_last))

# 判断法定节假日是不是调休
from chinese_calendar import is_in_lieu

date01 = datetime.date(2022, 1, 29)
date02 = datetime.date(2022, 2, 1)
print('is_in_lieu: ', is_in_lieu(date02))

print('datetime.date.today is_holiday: ', is_holiday(datetime.date.today()))
print('datetime.date.today is_holiday: ', is_workday(datetime.date.today()))