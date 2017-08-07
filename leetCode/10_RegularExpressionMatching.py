#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true
'''

'''
状态表示：d[i,j]，s匹配到i，p匹配到j，是否能匹配成功   例如d[1,1]=true  表示s字符串和p匹配都只取第一个字符能匹配成功

转移方程：

    pj为alpha:
        si=pj:d[i,j]=d[i−1,j−1]
        si≠pj:d[i,j]=0
    pj=∗:
        si=pj−1或pj−1=. : d[i,j]=d[i,j−2]||d[i−1,j] （分别代表：pj−1∗匹配空字符，匹配si，匹配至少1个。
        si≠pj−1且pj−1≠. : d[i,j]=d[i,j−2]（即si不能匹配当前的x*，那么我们直接认为x*为空字符）。
    pj=.:
        d[i,j]=d[i−1,j−1]
'''
def isMatch(s, p):
    # 定义状态 初始状态 i=0,j=0时空串匹配空串True  后面初始为False
    dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
    dp[0][0] = True
    # 初始化 i=0 j<>0的情况  即s是空串 此时p只能是 X*
    for j in range(1,len(p)):
        dp[0][j+1] = p[j]=='*' and dp[0][j-1]
    for i in range(len(s)):
        for j in range(len(p)):
            if s[i]==p[j]:
                dp[i+1][j+1]=dp[i][j]
            elif p[j]=='.':
                dp[i+1][j+1]=dp[i][j]
            elif p[j]=='*':
                # 如果*前面的字符和s当前字符不相等   此时 X* 表示0个x能否匹配取决与X*前面的p能否和当前s匹配
                if s[i]<>p[j-1]:
                    dp[i+1][j+1] = dp[i+1][j-1]
                if s[i]==p[j-1] or p[j-1]=='.':
                    # 三个表达式分表表示  X* 代表 0个x  1个x   多个x     多个x时只要判断当前p和s之前的能匹配就行
                    dp[i+1][j+1] = dp[i+1][j-1] or dp[i+1][j] or dp[i][j+1]
                    # 当 X*需要匹配多个x时 当前能否匹配取决于当前p和 s之前的能否匹配  此时X*才会取多个X
    return dp[-1][-1]



if __name__ == '__main__':
    print isMatch('aab','c*a*b')
