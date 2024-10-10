"""
@FileName：test
@Description：
@Author：shenxinyuan
@Time：2024/8/26
"""
import re

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# 符合格式的邮箱地址
email1 = 'example@example.com'
match1 = re.match(pattern, email1)
print(match1)

# 不符合格式的邮箱地址（缺少顶级域名）
email2 = '   example@datagrand.com'
match2 = re.match(pattern, email2)
print(match2)

email_pattern = re.compile('^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
cai_niao_email_pattern = re.compile("^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")

# 符合格式的邮箱地址
email3 = '    example@example.com  '
match3 = email_pattern.search(email3.strip())
print(match3)

email_list = [
    "john.doe@example.com",
    "jane_smith@company.co.uk",
    "alice.brown123@domain.net",
    "bob_456@sub.domain.org",
    "carol%789@test.io",
    "david.wilson@my-domain.info",
    "emma_jones@another-domain.biz",
    "frank%123@example.us",
    "grace.lee@domain123.tech",
    "harry_potter@wizard.world",
    "    example@example.com  ",
]
for email in email_list:
    # print("email_pattern:  "+str(email_pattern.match(email)))
    print("email_pattern:  "+str(email_pattern.search(email.strip())))
    # print("cai_niao_email_pattern:  "+str(cai_niao_email_pattern.match(email)))
    print("cai_niao_email_pattern:  "+str(cai_niao_email_pattern.search(email.strip())))



