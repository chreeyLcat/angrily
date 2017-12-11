# -*- coding:utf-8 -*-
'''
作者：jin
时间：2017-12-11
说明：二次封装的requests请求，公共方法
'''
import requests
import json


def postrequest(url, testdata, headers):
    # 以POST的方式进行请求，并把返回数据存到r这个变量里
    r = requests.post(url, data=testdata, headers=headers)
    # 把r的text的属性内容转换为json格式，并重新赋值给R
    r = json.loads(r.text)
    # 测试数据和返回数据做对比
    print(r)
    if testdata == r["data"]:
        print("测试通过！！！")
    else:
        print("测试不通过！！！")
        print(r["data"])
