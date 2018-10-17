"""
中文unicode案例
"""
import re
hello = u"你好，世界"
pattern = re.compile(r"[\u4e00-\u9fa5]+")

s = pattern.findall(hello)
print(s)

