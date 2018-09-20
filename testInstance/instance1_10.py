#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
instance1
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
def instance1_test1():
    d=[];
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if(i!=j) and j!=k and i!=k:
                    d.append([i,j,k])
    print '总数量:',len(d)
    print d

def instance1_test2():
    list_num=[1,2,3,4]
    list = [100*i+10*j+k for i in list_num  for j in list_num for k in list_num if(i!=j and j!=k and i!=k)]
    print list
    print len(list)

def instance1_test3():
    list = []
    for num in range(123,433):
        a = (num%1000)//100     #true除法 不管分子分母是什么类型商都只取最大的整数
        b = (num%100)//10
        c = num%10
        if a!=b and b!=c and a!=c and 0<a<5 and 0<b<5 and 0<c<5:
            print num
            list.append(num)
    print list

'''
instance2
'''
def instance2_test1():
    num=long(raw_input('净利润：'))
    arr=(1000000,600000,400000,200000,100000,0)
    rate=[0.01,0.015,0.03,0.05,0.075,0.1]
    result=0
    for i in range(0,6):
        if(num>arr[i]):
            result += (num-arr[i])*rate[i]
            num=arr[i]
    print result

def instance2_test2():
    num = long(raw_input('净利润：'))
    if(num<=10000*10):
        print num*0.1
    elif(num>10000*10 and num<=10000*20):
        print (num-10000*10)*0.075+10000*10*0.1
    elif(num>10000*20 and num<=10000*40):
        print (num-10000*20)*0.05+10000*10*0.05+10000*20*0.175
    elif(num>10000*40 and num<=10000*60):
        print (num-10000*40)*0.03+10000*40*0.225
    elif(num>10000*60 and num<=10000*100):
        print (num-10000*60)*0.015+10000*60*0.255
    else:
        print (num-10000*100)*0.01+10000*100*0.27

'''
instance3
1、则：x + 100 = n2, x + 100 + 168 = m2
2、计算等式：m2 - n2 = (m + n)(m - n) = 168
3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
7、接下来将 i 的所有数字循环计算即可。
'''
def instance3_test1():
    for i in range(1,85):
        if 168%i==0:
            j=168/i
            if i>j and (i+j)%2==0 and (i-j)%2==0:
                m=(i+j)/2
                n=(i-j)/2
                print n*n-100

'''
instance4
'''
def instance4_test1():
    year=int(raw_input('年:'))
    month=int(raw_input('月:'))
    day=int(raw_input('日:'))
    month_days=(31,28,31,30,31,30,31,31,30,31,30,31);
    result=0
    for i in range(1,month):
        result+=month_days[i-1]
    if ((year%4==0 and year%100!=0) or year%400==0) and month>2:
        result+=1
    result+=day
    print resul3
'''
instance5
'''
def instance5_test1():
    l=[]
    for i in range(3):
        a=int(raw_input('int:'))
        l.append(a)
    l.sort()
    print l

def instance5_test2():
    x=int(raw_input('x:'))
    y=int(raw_input('y:'))
    z=int(raw_input('z:'))
    a={'x':x,'y':y,'z':z}
    for i in sorted(a,key=a.get):
        print i,a[i]

'''
instance6 佩波那锲数列  0、1、1、2、3、5、8、13、21
'''
def instance6_test1(n):
    if(n==0):
        return 0;
    if(n==1):
        return 1;
    return instance6_test1(n-1)+instance6_test1(n-2)

def instance6_test2(n):
    if(n==0):
        return 0
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a

def instance6_test3(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])    #-1指取倒数第一个元素  -2表示倒数第二个元素
    return fibs

'''
instance7  数据复制
'''
def instance7_test1():
    a=[1,2,3]
    b=a[:]  #a[:]生成一个新对象，b指向新对象   b=a是b直接指向a
    a.append(4)
    print b
    print a

def instance7_test2():
    a=[1,2,3]
    import copy
    b=copy.copy(a)
    a.append(4)
    print a,b

'''
instance8   9*乘法表
'''
def instance8_test1():
    for i in range(1,10):
        print
        for j in range(1,i+1):
            print '%d*%d=%d' % (j,i,i*j),   #末尾加逗号不换行

'''
instance9  暂停一秒输出
'''
def instance9_test1():
    import time
    a=(1,2,3,4,5)
    for i in range(len(a)):
        print a[i]
        time.sleep(1)

'''
instance10   暂停一秒输出，并格式化当前时间
'''
def instance10_test1():
    import time
    print time.strftime('%Y-%m-%d %I:%M:%S',time.localtime(time.time()))
    time.sleep(1)
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

if __name__ == '__main__':
    instance10_test1()