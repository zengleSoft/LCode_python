#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        sign = (dividend < 0) is (divisor < 0)
        dividend,divisor = abs(dividend),abs(divisor)
        res = 0
        while dividend>=divisor:
            # 初始化 除数  倍数从1开始
            tmp,i = divisor,1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                # 左移，不会超范围，相当于*2 扩大倍数 降低时间复杂度
                i <<= 1
                tmp <<= 1
        if not sign: res = 0-res
        # 防止 -2147483648/-1  超范围
        return min(res,2147483647)

if __name__ == '__main__':
    self = Solution()
    print self.divide(-100,-2)
    i = 2
    i <<= 1
    print i

