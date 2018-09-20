#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
instance31
'''
def instance31_test1():
    letter=raw_input('第一个字母：')
    if letter=='m':
        print 'monday---星期一'
    elif letter=='w':
        print 'wednesday---星期三'
    elif letter=='f':
        print 'friday---星期五'
    elif letter=='t':
        secLetter=raw_input('第二个字母：')
        if secLetter=='u':
            print 'tuesday---星期二'
        elif secLetter=='h':
            print 'thursday---星期四'
    elif letter=='s':
        secLetter=raw_input('第二个字母：')
        if secLetter=='a':
            print 'saturday---星期六'
        elif secLetter=='u':
            print 'sunday---星期天'

'''
instance32
'''
def instance32_test1():
    a=[1,2,3,4,5,6]
    for i in a[::-1]:   #冒号前两个参数表示处理位置 没写表示从头到尾  第三个参数负数表示倒序  1表示每次序列加1  如果是2表示隔一个取一次
        print i

'''
instance33
'''
def instance33_test1():
    a=[1,2,3,4,5,7,8]
    s=','.join(str(i) for i in a)   #join函数 将元祖、列表按分隔符组成一个新的字符串
    print s

'''
instance35
'''
def instance35_test1():
    print '\033[93m'+'警告颜色字体？'+'\033[0m'

'''
instance36 输出指定范围内的素数
'''
def instance36_test1():
    start=int(raw_input('start:'))
    end=int(raw_input('end:'))
    r=[]
    for i in range(start,end+1):
        if i>1:
            for j in range(2,i):
                if(i%j==0):
                    break
            else:print i    #for-else  如果没有任何break退出则执行else，否则不执行

'''
instance37   选择排序
'''
def instance37_test1():
    a=[9,8,7,6,5,4,3,2,1,0]
    for i in range(len(a)-1):
        minIndex=i
        for j in range(i+1,len(a)):
            if a[j]<a[minIndex]:
                minIndex=j
        a[i],a[minIndex]=a[minIndex],a[i]
    print a

'''
instance39
'''
def instance39_test1(n):
    a=[1,3,5,7,9,11,13,15,17,19]
    a.append(n)
    l=len(a)
    while a[l-1]<a[l-2] and l>1:
        a[l-1],a[l-2]=a[l-2],a[l-1]
        l-=1
    print a

def instance39_test2(n):
    a=[1,3,5,7,9,11,13,15,17,19]
    if a[-1]<n:
        a.append(n)
    else:
        index=0
        while a[index]<n and index<len(a)-1:
            index+=1
        a.insert(index,n)
    print a

'''
instance40
'''
def instance40_test1():
    n=[1,3,5,7,9,11,13,15,17,19]
    for i in range(1,len(n)+1):
        print n[0-i],

def instance40_test2():
    n=[1,3,5,7,9,11,13,15,17,19]
    print n[::-1],

if __name__ == '__main__':
    instance40_test2()