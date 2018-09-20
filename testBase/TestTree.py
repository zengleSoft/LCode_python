#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/6/26

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def connect(root):
    import queue
    q1 = queue.Queue()
    q2 = queue.Queue()
    if root: q1.put(root)
    while not q1.empty():
        node1 = q1.get()
        while not q1.empty():
            node2 = q1.get()
            node1.next = node2
            if node1.left: q2.put(node1.left)
            if node2.right: q2.put(node1.right)
            node1 = node2
        node1.next = None
        if node1.left: q2.put(node1.left)
        if node1.right: q2.put(node1.right)
        q1 = q2


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    res = 0
    for lineIndex, line in enumerate(grid):
        for index, val in enumerate(line):
            if lineIndex == 0:
                if val == '1' and (index == 0 or line[index - 1] != '1'):
                    res += 1
            else:
                if val == '1' and grid[lineIndex - 1][index] != '1':
                    if index == 0 or line[index - 1] != '1':
                        res += 1
    return res


def serialize(root):
    """Encodes a tree to a single string.

    :type root: TreeNode
    :rtype: str
    """
    if not root:
        return '#,'
    s = ''
    s += str(root.val) + ','
    s += serialize(root.left)
    s += serialize(root.right)
    return s


def deserialize(data):
    """Decodes your encoded data to tree.

    :type data: str
    :rtype: TreeNode
    """

    def preOrder(l):
        val = l.pop()
        if val == '#':
            return None
        root = TreeNode(val)
        root.left = preOrder(l)
        root.right = preOrder(l)
        return root

    l = data.split(',')
    l = l[::-1]
    return preOrder(l)

if __name__ == '__main__':
    root = TreeNode(1)
    tmp = TreeNode(3)
    tmp.left = TreeNode(4)
    tmp.right = TreeNode(5)
    root.left = TreeNode(2)
    root.right = tmp
    x = serialize(root)
    print(x)
    a = deserialize(x)
    print(a)