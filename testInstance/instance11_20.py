#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
instance11  当月的兔子数等于上月兔子数+新增的数量  新增的数量=能生兔子的数=上月兔子数
'''
def instance11_test1(n):
    if n==1 or n==2:
        return 1
    else :
        return instance11_test1(n-1)+instance11_test1(n-2)

'''
instance12  输出101-200的素数
'''
def instance12_test1():
    import math
    for i in range(101,201,2):
        #判断是不是素数
        tmp = math.sqrt(i)
        for j in range(3,int(tmp)+1):
            if(i%j==0):
                break
            if(j==int(tmp)):
                print i,

'''
instance13   水仙花数
'''
def instance13_test1():
    for i in range(100,1000):
        a=i/100
        b=(i-a*100)/10
        c=i%10
        if a**3+b**3+c**3==i:
            print i

'''
instance14 分解质因数
'''
def instance14_test1(n):
    if n in[1]:
        print '{}'.format(n)
    while n not in [1]:
        for index in xrange(2,n+1):
            if n%index==0:
                n /=index
                if n==1:
                    print index
                else:
                    # print '{} *'.format(index),
                    print '%d *'%index,
                break

'''
instance15
'''
def instance15_test1(n):
    if n>=90:
        print 'A'
    else:
        print ('C','B')[n>=60]

'''
instance16 输出指定格式的日期
'''
def instance16_test1():
    import datetime
    print (datetime.datetime.today().strftime('%d/%m/%y'))
    #创建日期对象
    a=datetime.date(1949,10,1)
    print a.strftime('%Y-%m-%d')
    a=a+datetime.timedelta(days=30)
    print a.strftime('%Y-%m-%d')
    a=a.replace(year=a.year)
    print a.strftime('%Y-%m-%d')



if __name__ == '__main__':
    instance16_test1()