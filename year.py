# -*-coding：utf-8 -*-
'''
时间：2017-11-16
作者：chreey
作用：计算今天是一年中的第几天

year=int(input('请输入年:'))
month=int(input('请输入月:'))
day=int(input('请输入天:'))
sum=day
days = [31,28,31,30,31,30,31,31,30,31,30,31]
i=0
if ( year%4 == 0 and year%100 != 0) or (year%400 == 0):
    days[1] = 29
while i< month-1:
     sum=sum+days[i]
     i+=1
print('这一天是该年的第',sum,'天')

'''
timedate = [31,28,31,30,31,30,31,31,30,31,30,31]
print("欢迎使用时间计算系统")
year = input("请输入年份：")
month = input("请输入月份：")
day = input("请输入日期：")
days = 0
if int(year) % 4 == 0 | int(year) % 400 == 0:
    timedate[1] = timedate[1] + 1
    for i in range(int(month) - 1):
        days += timedate[i]
    days =  days + int(day)
    print("你好，%s-%s-%s是%s年的第%s天!" %(year,month,day,year,days))
else:
    for i in range(int(month) - 1):
        days += timedate[i]
    days =  days + int(day)
    print("你好，%s-%s-%s是%s年的第%s天!" %(year,month,day,year,days))   