#!/usr/bin/python
# -*- coding: UTF-8 -*-


'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
:type l1: ListNode
:type l2: ListNode
:rtype: ListNode
"""
def mergeTwoLists(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val<l2.val:
        l1.next = mergeTwoLists(l1.next,l2)
        return l1
    else:
        l2.next = mergeTwoLists(l2.next,l1)
        return l2

def mergeTwoLists2(l1,l2):
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next

if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(5)
    l2 = ListNode(2)
    print mergeTwoLists2(l1,l2)


