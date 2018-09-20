#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    if not head or not head.next:
        return head
    # 交换头节点和次节点的指向
    tmp_node = head.next
    head.next = head.next.next
    tmp_node.next = head
    # head变成次节点 递归调用剩下的节点
    head.next = swapPairs(head.next)
    # 此时tmp变成头节点 返回
    return tmp_node

def swapPairs2(self,head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    print swapPairs2(ListNode(0),head)