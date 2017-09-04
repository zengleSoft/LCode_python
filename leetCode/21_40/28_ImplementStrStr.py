#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 Implement strStr().
Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
判断 needle是否是haystack的子串
kmp 算法
'''

class Solution(object):
    # 35ms
    def strStr(self,haystack,needle):
        if not needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if needle==haystack[i:i+len(needle)]:
                return i
        else:return -1

if __name__ == '__main__':
    self = Solution()
    print self.strStr('a','a')