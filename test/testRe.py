# -*- codeing = utf8 -*-
# @Time 2020/9/14 10:45
# @Author : xxx
# @File : testRe.py
# @Software: PyCharm
import re


pat = re.compile("AA")
m = pat.search("CBA")
print(1, m)
m = pat.search("CBAAAA")
print(2, m)

#没有模式对象
#前面是正则 后面是字符串
m = re.search("asd", "ffasdkkk")
print(3, m)

#前面是正则，后面是字符串
print(4, re.findall("a", "fsllakkf"))
print(5, re.findall("[A-Z]+","ASfsfsAFA"))

#sub
#找到a用A替换
print(6, re.sub("a", "A", "afdkafdsa"))

#原生字符串
print(7, r"\a\fsafaa")