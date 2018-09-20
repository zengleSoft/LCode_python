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
    pass




if __name__ == '__main__':
    instance13_test1()