#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Example1: x = 123, return 321
# Example2: x = -123, return -321

# The input is assumed to be a 32 - bit signed integer.Your function should return 0 when  the reversed integer overflows.


def reverse(x):
    # 判断符号
    sign = cmp(x,0)
    #反引号转换成字符串  x*sign保证是正数
    r = int(`x*sign`[::-1])
    # 判断是否超处范围 和2的31次方比较大小
    return sign*r*(r < 2**31)




if __name__ == '__main__':
    print reverse(-8463847412)