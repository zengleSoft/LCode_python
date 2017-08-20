#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke"

# find the length of the longest substring without repeating characters
def lengthOfLongestSubstring(s):
    tmp = {}
    j = 0
    result = 0
    #i记录当前遍历元素的索引  j记录不重复的元素最近的索引    j保证当前正在计算的字符串不包含重复元素
    for i in range(len(s)):
        if s[i] in tmp:
            j = max(j,tmp[s[i]] + 1)
        tmp[s[i]]=i
        result = max(result,i-j+1)
    return result



if __name__ == '__main__':
    print lengthOfLongestSubstring('abba')

