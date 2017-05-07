#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
instance21
'''
def instance21_test1():
    sum = 1
    for i in range(1, 10):
        sum += 1
        sum *= 2
    print sum

'''
instance22
'''
def instance22_test1():
    # i、j、k代表xyz的出场顺序
    for i in range(ord('x'), ord('z') + 1):
        for j in range(ord('x'), ord('z') + 1):
            if i != j:
                for k in range(ord('x'), ord('z') + 1):
                    if i != k and j != k:
                        if i != ord('x') and k != ord('x') and k != ord('z'):
                            print 'order is a--%s\t b--%s\t c--%s' % (chr(i), chr(j), chr(k))

'''
instance23 打印菱形
'''
def instance23_test1():
    for i in range(1, 8):
        if (i <= 4):
            for j in range(4 - i):
                print ' ',
            for j in range(2 * i - 1):
                print '*',
        else:
            for j in range(i - 4):
                print ' ',
            for j in range(15 - 2 * i):
                print '*',
        print

'''
instance24
'''
def instance24_test1():
    a = 2.0
    b = 1.0
    s = 0
    for n in range(1, 21):
        s += a / b
        print '%d--%d' % (a, b)
        a, b = a + b, a
    print s

'''
instance25
'''
def instance25_test1():
    tmp = 1     #记录上一次阶乘值
    sum = 0     #记录总和
    for n in range(1, 21):
        tmp *= n
        sum += tmp
    print sum

'''
instance26
'''
def instance26_test1(n):
    if n==1:
        return 1
    else:
        return n*instance26_test1(n-1)

'''
instance27
'''
def instance27_test1(s):
    if(len(s)>0):
        print s[-1]
        instance27_test1(s[0:-1])   #截取字符串

'''
instance28
'''
def instance28_test1(n):
    if n==1:
        return 10
    else:
        return instance28_test1(n-1)+2

'''
instance29
'''
def instance29_test1(n):
    a=str(n)
    print '位数：%d'%len(a)
    b=[]
    while len(a)>0:
        b.append(a[-1])
        a=a[0:-1]
    print '逆序排列：',
    print b

'''
instance30   判断回文数
'''
def instance30_test1(n):
    a=n/10000
    b=(n/1000)%10
    c=n%1000/100
    d=n%100/10
    e=n%10
    if a==e and b==d:
        return True
    else: return False




if __name__ == '__main__':
   print instance30_test1(23432)
