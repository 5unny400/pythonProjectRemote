import unittest

import pandas as pd
import numpy as np
import pytest
from decimal import Decimal


class CreditBankFlowAnalysisTest(unittest.TestCase):

    def sample_data(self):
        data = {
            "oppo_account_name": ["A", "A", "B", "B", "C", "D", "D", "E"],
            "abs_trade_amount_decimal_precise": [Decimal("10.0"), Decimal("20.0"), Decimal("1.23"), Decimal("0.1"), Decimal("0.00"), Decimal("0.1"), Decimal("1000000.0"), float(
                np.nan)],
        }
        return pd.DataFrame(data)

    def test_decimal_precise_calculation(self):
        merged_df = self.sample_data().copy()
        # 方式一： 旧的 存在 decimal 为 0 的时候报错的问题
        # merged_df["min_to_max_ratio"] = (
        #     merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"]
        #     .transform("min")
        #     .div(merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"].transform("max"))
        # )
        # print(merged_df)

        # 方式二：存在逻辑问题：np.where 函数的用法是根据条件返回相应的值，但是你的代码中第三个参数在条件为真时应该返回一个 Series 或标量，
        # 而不是执行的操作。此外，transform 函数返回的是一个 Series，所以直接调用 div 会对整个 Series 进行除法计算，可能会导致计算错误。
        # 获取分母的最大值
        # max_values = merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"].transform("max")
        # merged_df["min_to_max_ratio"] = np.where(
        #     max_values != 0,
        #     merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"]
        #     .transform("min")
        #     .div(max_values)
        #     , 0
        # )
        # print(merged_df)

        # 方法三： OK  处理了 0 结果为 0 ，nan 值结果直接是 nan
        # max_values = merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"].transform("max")
        # max_values = max_values.replace(Decimal("0.0"), Decimal("1.0"))
        # merged_df["min_to_max_ratio"] = (
        #     merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"]
        #     .transform("min")
        #     .div(max_values)
        # )
        # print(merged_df)

        # 方式四：OK 处理了 0 结果为 nan，nan 值结果直接是 nan
        # max_values = merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"].transform("max")
        # merged_df["min_to_max_ratio"] = merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"].transform("min")
        # # 检查除数是否为零，将结果设为 NaN 或其他值
        # merged_df.loc[max_values != 0, "min_to_max_ratio"] /= max_values
        # merged_df.loc[max_values == 0, "min_to_max_ratio"] = np.nan
        # print(merged_df)

        # 方式五：OK 处理了 0结果为 0 ，nan 值结果直接是 nan（）
        # 使用 Decimal 类型进行除法操作，并处理除数为 0 的情况
        merged_df["min_to_max_ratio"] = (
            merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"]
            .transform(lambda x: min(x) / max(x) if max(x) != 0 else Decimal(0))
        )
        print(merged_df)
        # values = 0.08130081300813008130081300813 + 0.1
        # print(values)

    def test_float_calculation(self):
        merged_df = self.sample_data().copy()
        merged_df["abs_trade_amount_decimal_precise"] = merged_df["abs_trade_amount_decimal_precise"].astype(float)
        merged_df["min_to_max_ratio"] = (
            merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"]
            .transform("min")
            .div(merged_df.groupby("oppo_account_name")["abs_trade_amount_decimal_precise"].transform("max"))
        )
        print(merged_df)
        # 在 Pandas 中，当使用 `div` 函数进行除法运算时，对于除数为 0 的情况，Pandas 会自动将结果设为 NaN，而不会引发错误。这是因为
        # Pandas 在设计时考虑到了数据处理中常见的情况，希望在遇到异常情况时能够优雅地处理，而不是中断整个运算过程。

        try:
            print("使用 float 类型进行计算：", (1.23 / 0.1))
            print("使用 float 类型进行计算：", (1.23 / 10.0))
            print("除数为 0 使用 float 类型进行计算：", (1.23 / 0.00))
        except ZeroDivisionError:
            print("除数不能为 0")
