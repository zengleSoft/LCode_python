#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
'''

def letterCombinations( digits):
    if '' == digits: return []
    kvmaps = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    # reduce 对序列dights中的每个元素调用一个二元函数  第三个参数可选作为第一次调用时的初始值
    return reduce(lambda res,digit:[x+y for x in res for y in kvmaps[digit]],digits,[''])

if __name__ == '__main__':
    print letterCombinations('23')
