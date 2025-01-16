"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2025/1/16
"""
import pandas as pd
@staticmethod
def get_score_by_10_step(num):
    intervals = pd.IntervalIndex.from_tuples([
        (0, 10), (10, 20), (20, 30), (30, 40), (40, 50),
        (50, 60), (60, 70), (70, 80), (80, 90), (90, 100)
        ], closed='right')
    scores = [100, 80, 70, 60, 50, 40, 30, 20, 10, 0]

    for interval, score in zip(intervals, scores):
        if num in interval:
            return score

    print("error num[{}]".format(num))


if __name__ == "__main__":
    print(get_score_by_10_step(85))
    print(get_score_by_10_step(5))
    print(get_score_by_10_step(15))
    print(get_score_by_10_step(0))