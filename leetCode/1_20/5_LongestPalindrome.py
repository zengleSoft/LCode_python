#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 最长回文串  如果一个字符串 从左写和从右写都是一样的  那么这个字符串就是回文串

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input: "cbbd"
# Output: "bb"

def longestPalindrome(s):
    if len(s) < 2:
        return s
    # 将s每个字符间都填上#
    tmp = '#' + '#'.join(s) + '#'
    maxStr = s[-1]
    maxLength = 0
    for i in range(len(tmp)):
        # 以#为中心的回文串
        maxLength1 = 0
        if i % 2 == 0:
            a, b = i / 2 - 1, i / 2
            while a >= 0 and b < len(s):
                if s[a] == s[b]:
                    a -= 1
                    b += 1
                    maxLength1 += 2
                else:
                    break
            if maxLength < maxLength1 and a + 1 < b - 1:
                # 计算maxStr
                maxLength = maxLength1
                maxStr = s[a + 1:b]
        else:  # 以字符为中心左边第一个字符的回文串
            # 以字符为中心的回文串
            maxLength1 = 1
            c, d = (i - 3) / 2, (i + 1) / 2
            while c >= 0 and d < len(s):
                if s[c] == s[d]:
                    c -= 1
                    d += 1
                    maxLength1 += 2
                else:
                    break
            if maxLength < maxLength1 and c + 1 < d - 1:
                maxLength = maxLength1
                maxStr = s[c + 1:d]
    return maxStr

# 时间复杂度O(n)  http://www.cnblogs.com/bitzhuwei/p/Longest-Palindromic-Substring-Part-II.html
def longestPalindrome2(s):
    if len(s) < 2:
        return s
    s = '#' + '#'.join(s) + '#'
    p = []
    #记录比较过程中右边能到达的最远地方 以及到达最远地方时的中心点
    rightMax,mid = 0,0
    maxPval = 0
    maxPidx = 0
    for i in range(len(s)):
        # 比较过的最右边大于当前比较索引时才有可能减少比较次数
        if rightMax > i:
            # i关于mid的对称点
            i2 = 2*mid-i
            if p[i2] < rightMax-i:
                # 可以直接根据对称点的p值得到  跳出循环
                p.append(p[i2])
                continue
            else:
                # 从没有遍历到的地方开始遍历 不用从左边第一个开始比较
                start = 2*i - rightMax - 1
        else:
            # 这种情况只能从左边第一个开始比较  回文串只记录左边索引  左右索引关系 ：end - i = i - start
            start = i - 1
        while start >= 0 and 2 * i - start < len(s) and s[start] == s[2 * i - start]:

            if 2*i - start > rightMax:
                rightMax = 2*i - start
                mid = i
            start -= 1
        # 记录p中最大值
        if maxPval<i-start-1:
            maxPval = i-start-1
            maxPidx = i
        p.append(i - start - 1)
    begin,end = maxPidx-maxPval,maxPidx+maxPval
    result = s[begin:end+1]
    return result.replace('#','')


if __name__ == '__main__':
    print (longestPalindrome2('babcbabcbaccba'))
    print (longestPalindrome('babcbabcbaccba'))
