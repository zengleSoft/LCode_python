#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/3/4
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.



Example:

Input: "cbbd"

Output: "bb"

'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in xrange(len(s)):
            # 以 s[i]为中心的奇数回文串
            tmp = self.palindrome(s,i,i)
            if len(tmp)>len(res):res=tmp
            # 以s[i] 和 s[i+1]为中心的偶数回文串
            tmp = self.palindrome(s,i,i+1)
            if len(tmp)>len(res):res=tmp
        return res


    # 从中间向两边寻找回文串
    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
