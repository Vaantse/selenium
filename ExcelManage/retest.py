# -*- coding:utf-8 -*-
__author__ = "Cydonia"
import re

# str = input("请输入email:")
#
# if re.match(r'^\w+@\w+.[a-zA-Z]+$', str):
#     print('ok')
# else:
#     print('failed')

# url = input("请输入url:")
#
# print(url.split('.')[-1])

# mailName_re = re.compile(r'(<\w+ \w+>) (\w+@\w+.\w+)')
#
# print(mailName_re.match('<Tom Paris> tom@voyager.org').groups())

# XMLStr = '<book>python</book>'
#
# if re.match(r'<(\w+>)\w+</\1', XMLStr):
#     print('ok')
# else:
#     print('failed')
#
# from datetime import datetime, timedelta
#
# now = datetime.now()
# now = now + timedelta(days = -1)
# print(now.strftime('%Y-%m-%d'))

str = input("请输入email:")

email_re = re.compile(r'\w|.+@\w+.com')
if email_re.match(str):
    print('ok')
else:
    print("failed")