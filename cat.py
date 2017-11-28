# -*- coding：utf-8 -*-
'''
时间：2017-11-25
作者：chreey
作用：学习
print("hello world")
str = "自定义变量名，string的缩写str" # 字符串
num = "11111" #数字
list = [1, 2, 3, "四", "五"] # 数组
dict = {"a":"啊", "b":"波"} # 字典
float =3.1314 # 浮点
null = None # 空，不存在
print(type(str))

'''
for i in range(4):
    if i != 3:
        print("------------------------")
        print("|                       |")
        print("|     欢迎来到咪咕会    |")
        print("|                       |")
        print("------------------------")
        username = input("请输入用户名：")
        if username == "cat":
            password = input("请输入密码: ")
            if password == "123456":
                print("登录成功")
                break
            else:
                print("密码错误,请重新登录")
        
        else:
            print("账户不存在！")
    else:
        print("错误操作超过三次，请联系管理员!!!")
        exit()
user = {"name": username, "age": "18岁", "high": " 168cm", "job": "测试工程师", "sex": "女"}
for key in user:
    print(key, ":\t", user[key])
 

