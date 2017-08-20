#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Given a roman numeral, convert it to an integer.

# Input is guaranteed to be within the range from 1 to 3999.


def romanToInt(s):
    M = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    sum = 0
    for i in range(len(s)-1):
        # 如果字符串前面的单位小于后面的 那就是减去单位
        if M[s[i]] < M[s[i+1]]:
            sum -= M[s[i]]
        else:
            sum += M[s[i]]
    # 最后一位一定是加
    return sum + M[s[-1]]