#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

'''
python优先级队列 默认自然序 越小越先出 列表类都是按第一个元素排序 对象不能排序的按put顺序出
'''
def mergeKLists(lists):
    from Queue import PriorityQueue
    q = PriorityQueue()
    cur = ListNode(0)
    res = cur
    for node in lists:
        if node:
            q.put((node.val,node))
    while not q.empty():
        cur.next = q.get()[1]
        cur = cur.next
        if cur.next:
            q.put((cur.next.val,cur.next))
    return res.next



if __name__ == '__main__':
    l = ListNode(0)
    l.next = ListNode(2)
    l.next.next = ListNode(5)
    print mergeKLists([l])
