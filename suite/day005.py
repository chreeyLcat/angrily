# -*- coding:utf-8 -*-
'''
作者：浪晋
时间：2017-12-5
说明：演示requests的基本用法
'''
from tools import requesttool


def testcase001(testdata):
    # 输入测试的接口地址
    url = "https://postman-echo.com/post"
    # 输入headers
    headers = {
        'content-type': "text/plain"
        }
    requesttool.postrequest(url, testdata, headers)


testdata1 = "hello world!"
testdata2 = "hello python!"
testdata3 = "hello java!"
testdatalist = [testdata1, testdata2, testdata3]
for testdata in testdatalist:
    testcase001(testdata)
