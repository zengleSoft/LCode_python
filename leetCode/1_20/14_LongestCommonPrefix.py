#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    maxStr = strs[0]
    if len(strs) == 1:
        return maxStr
    flag = True
    for str in strs:
        if len(str) == 0 or len(maxStr)==0:
            return ''
        i = 0
        while i<len(str) and i<len(maxStr) and maxStr[i] == str[i]:
            flag = False
            i += 1
        maxStr = str[0:i]
    if flag:
        return ''
    return maxStr


def longestCommonPrefix2(strs):
    if len(strs)==0:
        return ''
    strs=sorted(strs)
    i = 0
    # 排序后只需要比较第一个和最后一个字符的公共前缀
    while len(strs[0])>0 and i<len(strs[0]) and strs[0][i]==strs[-1][i]:
        i+=1
    if i==0:
        return ''
    return strs[0][0:i]


def longestCommonPrefix3(strs):
    if not strs:
        return ''
    # zip函数 接受任意多个序列  返回一个元祖列表  其中每个元祖都是序列对应位置的元素
    for i,letter_group in enumerate(zip(*strs)):
        # set集合 传入序列 去重  返回非重复的元素
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else: # for-else 结构
        return min(strs)



if __name__ == '__main__':
    s = ['xabc','derf','fdc']
    longestCommonPrefix3(s)
    # for i,a in enumerate(s):
    #     print i
    #     print a
    # print zip(*s)
    # print s
    print (set(('x','x','d')))