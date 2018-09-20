#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''


class Listnode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self,head,k):
        if not head or k<2:
            return head
        tail_head = head
        for i in range(k-1):
            tail_head = tail_head.next
            if not tail_head:
                return head
        tmp,cur = None,head
        for i in range(k):
            tmp_next = cur.next
            cur.next = tmp
            tmp = cur
            cur = tmp_next
        head.next = self.reverseKGroup(cur,k)
        return tail_head



    if __name__ == '__main__':
        pass
