#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/3/4
'''
 Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s, carry, i, j = '', 0, len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry==1:
            carry += int(a[i]) if i>=0 else 0
            i-=1
            carry += int(b[j]) if j>=0 else 0
            j-=1
            s = str(carry%2)+'0' + s
            carry /= 2
        return s



    def addBinary(self, a, b):
        # return bin(eval('0b'+a)+eval('0b'+b))
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    self = Solution()
    print self.addBinary('0','0')
