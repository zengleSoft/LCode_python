#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Determine whether an integer is a palindrome. Do this without extra space.

def isPalindrome(x):
    if x<>0 and x%10==0:
        return False
    rev = 0
    # 当 x<=rev时说明已经x反转一半
    while x>rev:
        # 将x的个位记录到res的高位
        rev = rev*10 + x%10
        # x去掉个位数
        x = x/10
    return (x==rev or x==rev/10)