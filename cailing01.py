# -*- coding：utf-8 -*-
'''
time:2017-12-06
author:chreey
annotation:彩铃banner
'''
import requests
import json


def case01(querystring):
    url = "http://218.200.227.207:18089/MIGUM2.0/v1.0/content/querycontentbyId.do"

    headers = {
        'msisdn': "13577201811",
        'test': "01",
        'cache-control': "no-cache",
        'postman-token': "f7fedb69-6a8e-8f2e-5ee4-842ad81a1a2a"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        content = json.loads(response.text)
        print(content)

        if "000000" == content["code"]:
            print("测试通过！！")
        else:
            print("测试不通过！")
            print(response.text)
    else:
        print(response.status_code)


querystring = {"ua": "Android_migu", "version": "5.0.0", "columnId": "19444079", "needAll": "0"}
case01(querystring)
