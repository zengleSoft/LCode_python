#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 格式化输出
def printStr():
    print 'my name is :%s and age is %d' % ('le',3)
    print 'float precision is %.1f' % 1.234
    print 'domain design float precision %.*f' % (5,1.2345667)

# 字符串拼接
def joinStr():
    print 'plus union str '+' test str'
    print '|'.join(['str1','str2','str3'])

    str1 = 'union'
    str2 = 'as a'
    str3 = 'tuple'
    s = str1,str2,str3
    print type(s)

# 字符串切割
def splitStr():
    # split函数默认分隔符是空格   第二个参数是分割多少个分割符
    list = 'abc cd'.split()
    print list
    list2 = 'abcd a d ge e'.split(' ',2)
    print list2

# 字符串替换
def replaceStr():
    # 1、旧字符串   2、新字符串    3、替换次数
    print 'abcdefgab'.replace('ab','xx',1)

# 字符串查找
def findStr():
    # 查找第一次出现的索引  没有返回-1
    print 'abcdefgcd'.find('q')
    # 返回bool类型
    print 'cd' in 'abcdef'

# 字符串分割操作
def cutStr():
    # 截取字符串1-2
    print 'abcded'[1:2]
    # 一共三个参数 ：隔开 第一个和第二个指定开头和结尾索引前闭后开不写表示从头到前   第三个参数表示间隔多少cut一个  负数表示从后往前
    print 'abcdefg'[::-2]


if __name__ == '__main__':
    replaceStr()