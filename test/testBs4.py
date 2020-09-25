# -*- codeing = utf8 -*-
# @Time 2020/9/13 21:27
# @Author : xxx
# @File : testBs4.py
# @Software: PyCharm

#BeautifulSoup4 将html文档转换成复制的树结构
import re
from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html = file.read()
bs = BeautifulSoup(html, "html.parser")

#BeautifulSoup代表整蛊文件
#print(bs)

#只能拿到第一个
#print(bs.title)
#print(bs.title.string)
#print(type(bs.title))

#文档的遍历
#print(bs.header.container)

#文档的搜索
#字符串过滤 查找所有a标签
#t_list = bs.find_all("a")
#print(t_list)

#正则表达式的搜索
#t_list = bs.find_all(re.compile("a"))
#print(t_list)

#函数搜索
# def name_is_exists(tag):
#     return tag.has_attr("href")
# t_list = bs.find_all(name_is_exists)
# print(t_list)

#kwargs 参数搜索
#t_list = bs.find_all(class_="about")
t_list = bs.find_all(href="http://www.usfca.edu")
print(t_list)

#3.text参数
#t_list = bs.find_all(text=["地图","贴吧"])
#t_list = bs.find_all(re.compile("\d") 应用正则表达式来查找

#4.limit 参数
#t_list = bs.find_all("a",limit=3)

#css选择器
#print(bs.select("title")) #标签
#print(bs.select(".nav")) #css 类
#print(bs.select("#idd")) #id
#print(bs.select("div[class='about']")) #属性
#print(bs.select("head > title")) #子标签
#t_list = (bs.select(".head ~ .menu")) #兄弟节点
#print(t_list[0].get_text())
