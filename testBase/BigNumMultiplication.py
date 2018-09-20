#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/5/9

'''
大数乘法
111111111111111   222222222222222
24691358024691308641975308642
24691358024691308641975308642
ab cd
(a*10**(len(str1)-mid1) + b)(c*10**(len(str2)-mid2) + d)
ac*10**(len(str1)+len(str2)-mid1-mid2) + ad*10**(len(str1)-mid1) + bc*10**(len(str2)-mid2) + bd
'''

def add(str1, str2):
    '''
    :param str1:
    :param str2:
    :return:String
    '''
    list1 = [int(i) for i in str1[::-1]]
    list2 = [int(i) for i in str2[::-1]]
    list = []
    for i in range(max(len(list1), len(list2))):
        if i > len(list1) - 1:
            list.append(list2[i])
            continue
        if i > len(list2) - 1:
            list.append(list1[i])
            continue
        list.append(list1[i] + list2[i])
    carry = 0
    for i in range(len(list)):
        tmp = (list[i] + carry)%10
        carry = (list[i] + carry)//10
        list[i] = str(tmp)
    if carry>0:
        list.append(carry)
    if list[-1]=='0':return '0'
    return ''.join(list[::-1])

def mutiplication(str1, str2):
    '''
    :param str1:
    :param str2:
    :return:String
    '''
    if not str1 or not str2:
        return '0'
    if str1[0] == '0' or str2[0] == '0':
        return '0'
    if len(str1) == 1 and len(str2) == 1:
        return str(int(str1) * int(str2))
    mid1, mid2 = len(str1) // 2, len(str2) // 2
    a = str1[0:mid1]
    b = str1[mid1:]
    c = str2[0:mid2]
    d = str2[mid2:]
    ac = mutiplication(a, c) + '0' * (len(str1) + len(str2) - mid1 - mid2)
    ad = mutiplication(a, d) + '0' * (len(str1) - mid1)
    bc = mutiplication(b, c) + '0' * (len(str2) - mid2)
    bd = mutiplication(b, d)
    return add(add(ac,ad) , add(bc,bd))






if __name__ == '__main__':
    print(mutiplication('1', '23'))
    list=[1,23]
    list[1] = 'aa'
    print(add('0','00'))
