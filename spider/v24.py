"""
search 练习
"""

import re
s = r'\d+'

pattern = re.compile(s)

m = pattern.search("one12two34three56")
print(m.group())

#参数表示搜查的起始范围

m = pattern.search("one12two34three56",10,40)
print(m.group())