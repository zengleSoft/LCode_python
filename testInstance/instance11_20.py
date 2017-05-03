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

'''
instance17
'''
def instance17_test1():
    import string
    str=raw_input('input a string：\n')
    letters,space,digit,other=0,0,0,0
    for c in str:
        if c.isalpha():
            letters+=1
        elif c.isspace():
            space +=1
        elif c.isdigit():
            digit+=1
        else:
            other+=1
    print 'letters=%d,space=%d,dight=%d,other=%d'%(letters,space,digit,other)

'''
instance18
'''
def instance18_test1():
    Tn=0
    Sn=[]
    n=int(raw_input('n='))
    a=int(raw_input('a='))
    for count in range(n):
        Tn += a
        a *= 10
        Sn.append(Tn)
        print Tn
    Sn=reduce(lambda x,y:x+y,Sn)
    print '和：',Sn

'''
instance19
'''
def instance19_test1():
    for i in range(3,1001):
        sum=0
        for j in range(1,i):
            if(i%j==0):
                sum+=j
        if(sum==i):
            print i

'''
instance20
'''
def instance20_test1():
    hei=100.0 #起始高度
    tim=10    #次数
    height=[]   #记录反弹高度
    tour=[]     #记录落地高度
    for i in range(1,tim+1):
        if(i==1):
            tour.append(hei)
        else:
            tour.append(2*hei)
        hei /=2
        height.append(hei)
    print '总高度：tour={0}'.format(sum(tour))
    print '第十次反弹高度：height={0}'.format(height[-1])

if __name__ == '__main__':
    instance20_test1()