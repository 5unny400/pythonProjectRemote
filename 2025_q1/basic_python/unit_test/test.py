"""
@FileName：test
@Description：使用 unittest.TestCase类时，方法要以 "test" 开头
@Author：shenxinyuan
@Time：2025/1/26
"""
# -*- coding: utf-8 -*-
import unittest


class CreditBankFlowAnalysisTest(unittest.TestCase):

    # 信贷流水对手方分析全部对手方
    def test_store_analysisi_result(self):
        print(f"{self._testMethodName}")


    def test_my_unittest(self):
        """
        测试用例
        :return:
        """
        # 打印当前类名
        print(f"{self.__class__.__name__}")
        # 打印当前方法名
        print(f"{self._testMethodName}")
        # 打印当前方法的注释
        print(f"{self._testMethodDoc}")

    def testmy_unittest(self):
        print(f"{self._testMethodName}")


    def my_unittest(self):
        print(f"{self._testMethodName}")


if __name__ == '__main__':
    # unittest.main() 会自动发现并运行 CreditBankFlowAnalysisTest 类中所有以 test 开头的方法。
    unittest.main()
