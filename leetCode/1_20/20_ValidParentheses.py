#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''


def isValid(s):
    tmp = []
    dic = {'(':')','[':']','{':'}'}
    for i in s:
        if i in dic:
            tmp.append(i)
        else:
            if not tmp or i != dic.get(tmp.pop()):
                return False
    if not tmp:
        return True
    else:
        return False

if __name__ == '__main__':
    print (isValid('()'))