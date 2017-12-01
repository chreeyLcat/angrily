# -*- coding：utf-8 -*-
'''
作用：我的第一个函数
'''


def user():
    '''
    第一个函数，没什么用处
    '''

    list = ["chreey", "joy", "tom"]
    people = {
        "chreey": {
            "age": 20,
            "high": 172,
            "sex": "boy"
        },
        "joy": {
            "age": 18,
            "high": 165,
            "sex": "gilr"
        },
        "tom": {
            "age": 12,
            "high": 160,
            "sex": "boy"
        }
    }
    for key in list:
        # print(people[key])
        print("姓名：%s，年龄：%s，身高：%s，性别：%s" % (key, people[key]["age"], people[key]["high"], people[key]["sex"]))


user()


def sumnun(a, b):
    print(a + b)


sumnun(9, 3)
