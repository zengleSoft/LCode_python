#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/6/19

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if not headA or not headB: return
    curA, curB = headA, headB
    cur, tmpCur = None, None
    while curA or curB:
        if curA == curB:
            return curA
        elif curA and curB:
            curA = curA.next
            curB = curB.next
        else:
            if curA:
                cur, tmpCur, tmpCur2 = curA, headA, headB
            else:
                cur, tmpCur, tmpCur2 = curB, headB, headA
            while cur:
                cur = cur.next
                tmpCur = tmpCur.next
            while tmpCur and tmpCur2 and tmpCur != tmpCur2:
                tmpCur = tmpCur.next
                tmpCur2 = tmpCur2.next
            return tmpCur
    return None


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(2)

    l2 = ListNode(3)

    print(getIntersectionNode(l1,l2))
    s= 1 if True else 3
    print(s)
