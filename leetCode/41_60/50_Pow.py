#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/3/4

'''
Implement pow(x, n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

'''


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if n < 0:
            x = 1 / x
            n = 0 - n

        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x * x, n / 2)


if __name__ == '__main__':
    self = Solution()
    print self.myPow(2, 1)
