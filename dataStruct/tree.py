#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/4/9

class tree(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

# 后续遍历非递归实现
def postOrder(root):
    stack=[]
    t = root
    while t or stack:
        while t:
            # 一直向左遍历并压栈
            stack.append(t)
            t = t.left
        if stack:
            # 弹出第一个左子树为空的元素
            t = stack.pop()
            # 如果没有右子树
            while not t.right:
                # 没有右子树且左子树为空 访问中间元素
                print(t.val)
                if stack: # 继续弹栈 开始上一层遍历
                    t = stack.pop()
                else:return # 刚访问完中间结点 如果栈空了表示遍历完了直接返回
            # 上面的while循环一直到第一个有右子树的结点 用一个tmp记录中间结点并压栈 然后继续从右子树开始
            tmp = tree(t.val)
            stack.append(tmp)
            t = t.right

# 前续遍历非递归实现
def preOrder(root):
    stack = []
    t = root
    while t or stack:
        while t:
            print(t.val)
            stack.append(t)
            t=t.left
        if stack:
            t = stack.pop()
            t = t.right

# 中续遍历非递归实现
def midOrder(root):
    stack = []
    t = root
    while t or stack:
        while t:
            stack.append(t)
            t = t.left
        if stack:
            t = stack.pop()
            print(t.val)
            t = t.right


if __name__ == '__main__':
    root = tree(1)
    rootLeft = tree(2)
    rootRight = tree(3)
    rootLeft.left = tree(4)
    rootLeft.right = tree(5)
    rootRight.left = tree(6)
    # rootRight.right = tree(7)
    root.left = rootLeft
    root.right = rootRight
    postOrder(root)