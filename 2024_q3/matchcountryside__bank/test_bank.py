"""
@FileName：test_bank
@Description：
@Author：shenxinyuan
@Time：2024/9/25
"""
import re

bank_name = ['中国银行股份有限公司石家庄市裕东支行', '中国建设银行股份有限公司荆州玉桥支行', '邯郸农商银行股份有限公司藁城支行', '兴业银行股份有限公司石家庄开发区科技支行', '张家口银行股份有限公司石家庄塔通路支行', '吉林九台村镇银行吉林市支行', '上海农商银行股份有限公司荆州分行', '招商银行股份有限公司荆州分行']
bank_pattern = re.compile("农商行|农商|村|镇")


def is_bank(bank_name_list):
    for bank_name in bank_name_list:
        if bank_pattern.search(bank_name):
            print(bank_name + "是村镇银行")


is_bank(bank_name)
