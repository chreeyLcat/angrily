# -*- coding：utf-8 -*-
'''
作用：自动化框架怎么来做配置文件,采用字典的方式
'''
from config import DeploymentConfig
from config import Testconfig
username = DeploymentConfig["username"]
print(username)
filehome = DeploymentConfig["filehome"]
print(filehome)
username = Testconfig["username"]
print(username)
filehome = Testconfig["filehome"]
print(filehome)
