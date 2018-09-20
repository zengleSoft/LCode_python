#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

def generateParenthesis(n):
    res = ['()'*n]
    if n==1:
        return res
    else:
        tmp = generateParenthesis(n-1)
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            if tmp[i][j]==')':
                res.append(tmp[i][0:j]+'()'+tmp[i][j:])
    res.sort()
    return res

'''
在字符串的任何位置只要保证前面的左括号数大于等于右括号数
'''
def generateParenthesis2(n):
    def generate(p, left, right, parens=[]):
        if left:       # 保证先补充左括号
            generate(p + '(', left - 1, right)
        if right > left:    # 如果右大于左 补充右括号
            generate(p + ')', left, right - 1)
        if not right:   # 如果right==0 表示一种已经生产完成
            parens += p,
        return parens
    return generate('', n, n)


def generateParenthesis3(n,open=0):
    if n > 0 <= open:
        return ['(' + p for p in generateParenthesis3(n - 1, open + 1)] + \
               [')' + p for p in generateParenthesis3(n, open - 1)]
    return [')' * open] * (not n)


if __name__ == '__main__':
    print(generateParenthesis2(3))

