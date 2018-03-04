#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/2/27

'''
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).  和leetcode10不同的地方 *可以表示所有

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
'''


class Solution(object):
    '''
    状态表示：d[i][j]，s匹配到i，p匹配到j，是否能匹配成功   例如d[1][1]=true  表示s字符串和p匹配都只取第一个字符能匹配成功

    转移方程：

        pj为alpha:
            si=pj : d[i,j]=d[i−1,j−1]
            si≠pj : d[i,j]=false
        pj=∗:
            因为*可以匹配任何字符串，所以只要看 d[x][j]是否有true 如果有当前就是true  x<i
            s：abcdefg   p:xxxxx*  如果 abcdef和xxxxx*不能匹配 且 abcdefg和xxxxx不能匹配 则 s和p肯定不能匹配
        pj=?:
            d[i,j]=d[i−1,j−1]
    '''

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        if p and p[0]=='*':dp[0][1]=True
        if p and p[0]<>'*':dp[0][1]=False
        for j in range(1,len(p)):
            dp[0][j+1] = p[j] == '*' and dp[0][j]

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j]=='?' or p[j]==s[i]:
                    dp[i + 1][j + 1] = dp[i][j]
                elif p[j]=='*':
                    if j-1>=0 and p[j-1]=='*':      # 如果j不是第一个且上一个也是*那么直接看当前s能否和上一个*之前的匹配
                        dp[i + 1][j + 1] = dp[i+1][j]
                    else:
                        dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
                        # # *可以取任何值 所以*之前的和任意当前s的子串能匹配的话当前p就能匹配
                        # for x in range(i+2):  # x要取到i+1
                        #     if dp[x][j]:
                        #         dp[i + 1][j + 1] = True
                        #         break
                        # else:
                        #     dp[i + 1][j + 1] = False

        return dp[-1][-1]

    def isMatch2(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        # 此时p是空  只有s取空时才为True
        dp = [True] + [False] * length
        for i in p:
            if i=='*':
                for n in range(1,length+1):
                    # 左边 dp[n-1]表示当前长度i和上一次s能否匹配   dp[n]表示当前长度的s和上一层i是否能匹配
                    dp[n] = dp[n-1] or dp[n]
            else:
                for n in reversed(range(length)):
                    # =右边的dp[n] 表示s取n个时和上一次循环的i能够匹配  如果不能匹配就时false  如果能匹配 就看当前的i是否能和s[n]匹配
                    dp[n+1] = dp[n] and (i==s[n] or i=='?')
            dp[0] = dp[0] and i=='*' # 除非当前i是*否则空s和能否匹配当前i和上一次i一样
        return dp[-1]

if __name__ == '__main__':
    self = Solution()
    print self.isMatch2('','')