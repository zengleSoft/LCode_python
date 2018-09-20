#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''


class Solution(object):
    '''
    dp 设置一个数组 存储末尾索引为i的字符串的匹配长度 如果是 (  这是0  如果是 )且上一个是( 那么res[i]=res[i-2]+2
    如果是 ) 且上一个也是 ) 那么从i-1向前回溯 res[i-1]如果是)那么res[i]=0  )(正常匹配))
    如果是 ( 那么看 (的上一个res值加上后面的就是i的res值
    '''
    def longestValidParentheses(self, s):
        if not s:
            return 0
        longest = [0 for i in s]
        res = 0
        for i in range(len(s)):
            if s[i] == ')':
                if s[i - 1] == '(':
                    longest.append(longest[i - 2] + 2)
                    res = max(res,longest[i])
                else:
                    if i - longest[i - 1] - 1>=0 and s[i - longest[i - 1] - 1] == '(':
                        longest.append(longest[i - longest[i - 1] - 1 - 1] + 2 + longest[i - 1])
                    elif i - longest[i - 1] - 1==0 and s[i - longest[i - 1] - 1] == '(':
                        longest.append(2 + longest[i - 1])
        return res

if __name__ == '__main__':
    self = Solution()
    print self.longestValidParentheses("(()())")
    longest = [0 for i in range(10)]
    print longest
