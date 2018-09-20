#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/1/17

'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contains only digits 0-9.
    Both num1 and num2 does not contain any leading zero.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    '''
          123
          234
    4 8 12
  3 6 9
2 4 6
    '''
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0': return '0'
        # 记录两个数字每一位相乘结果 不考虑进位
        tmp = [0 for _ in range(len(num1) + len(num2))]
        indexN1, indexN2 = 0, 0
        for n1 in reversed(num1):
            indexN1 += 1
            indexN2 = 0
            for n2 in reversed(num2):
                indexN2 += 1
                tmp[indexN1 + indexN2-2]=tmp[indexN1 + indexN2-2] + int(n1)*int(n2)
        result=''
        # 进位
        carry=0
        for index,val in enumerate(tmp):
            if index==len(tmp)-1 and val==0 and carry==0:break
            if val+carry <10:
                result = str(val+carry)+result
                carry=0
            else:
                result = str((val+carry)%10) + result
                carry = (val+carry)/10
        return result

if __name__ == '__main__':
    self = Solution()
    print self.multiply("123","234")
