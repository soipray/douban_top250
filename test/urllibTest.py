# -*- codeing = utf8 -*-
# @Time 2020/9/13 17:31
# @Author : xxx
# @File : urllibTest.py
# @Software: PyCharm
import urllib.request
import urllib.parse

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# #print(response.read().decode("utf-8"))
#
# #获取一个post请求
#
# data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)
# #print(response.read().decode("utf-8"))
#
# #超时
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.01)
#     #print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("timtout")
#

url = "http://www.douban.com"
data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
}
req = url.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))


