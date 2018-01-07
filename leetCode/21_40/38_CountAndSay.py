#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"

统计上一个字符串
'''
import itertools


class Solution(object):
    def countAndSay(self,n):
        if  n==1:return '1'
        previousVal = self.countAndSay(n-1)

        cur,cnt,result=0,0,''
        for index,val in enumerate(previousVal):
            if previousVal[cur]==val:
                cnt += 1
            else:
                result = result + str(cnt)+previousVal[cur]
                cur=index
                # 下一次循环将
                cnt=1
        result = result + str(cnt)+previousVal[cur]
        return result

    def countAndSay2(self, n):
        s = '1'
        for _ in range(n - 1):
            # for digit, group in itertools.groupby(s)
            s = ''.join( str(len(list(group))) + digit for digit, group in itertools.groupby(s) )
        return s

if __name__ == '__main__':
    s='1'

