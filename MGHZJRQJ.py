# -*- coding：utf-8 -*-
'''
time:2017-12-06
author:chreey
annotation:彩铃banner
'''
import requests
import json


def case02(querystring):
    url = "http://10.25.245.113:8080/MIGUM2.0/v1.0/activity2/syncUserVoterInfo.do"

    querystring = {"activity": "MGHZJRQJ", "activityStage": "03"}
    payload = "[{\"copyrightId\":\"63273400366\",\"contentId\":\"600907000003977608\",\"uid\":\"1cd6caec-23ad-4173-9322-e7af31754b66\",\"msisdn\":\"13578474393\",\"resourceType\":\"0\",\"totleCount\":\"2\",\"singerId\":\"1000000747\"}]"
    headers = {
        'channel': "014000D",
        'cache-control': "no-cache",
        'postman-token': "98296a6e-9bb3-8b91-da9e-afe05b8363b9"
        }
    response = requests.post(url, data=payload, headers=headers, params=querystring)
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
case02(querystring)
