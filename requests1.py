# -*- coding：utf-8 -*-
'''
作用：requests的基本用法
'''
import requests
import json

# get请求
# r = requests.get("https://www.baidu.com")
# print(r.headers)

# post请求
# 输入测试的接口地址
url = "https://postman-echo.com/post"
# 输入测试数据
testdata = "miaomi"
# 输入header
headers = {
    'content-type': "text/plain", 
    }
# 以post方式进行请求，并把返回数据存人r这个变量里
r = requests.post(url, data=testdata, headers=headers)
# 把r的text的属性内容转换为json格式，并重新赋值给r
r = json.loads(r.text)
# 测试数据和返回数据做对比
print(r["url"])
print(r["data"])
print(r["headers"])
if testdata == r["data"]:
    print("测试通过！！！")
else:
    print("测试不通过")
    print(r["data"])
