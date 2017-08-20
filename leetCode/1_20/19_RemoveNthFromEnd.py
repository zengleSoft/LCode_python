#!/usr/bin/python
# -*- coding: UTF-8 -*-



'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 空间换时间 将每个节点存到临时列表中
def removeNthFromEnd(head,n):
    # 存储每一个节点
    tmp = [head]
    tmp_node = head
    while tmp_node.next:
        tmp.append(tmp_node.next)
        tmp_node = tmp_node.next
    # 找出要删除的节点
    if len(tmp)<=n:
        head = head.next
    else:
        tmp[0 - n - 1].next = tmp[0 - n].next
    return head

# 两个指针 第一个先走n  然后两个一起走
def removeNthFromEnd2(head,n):
    slow,fast = head,head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head



if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    removeNthFromEnd(head,1)
