"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2025/1/17
"""


def case_match_age(age: int):
    match age:
        case x if 0 <= x < 10:
            print(f'< 10 years old: {x}')
        case 10:
            print('10 years old.')
        case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
            print('11~18 years old.')
        case 19:
            print('19 years old.')
        case _:
            print('not sure.')


case_match_age(0)
case_match_age(10)
case_match_age(20)
