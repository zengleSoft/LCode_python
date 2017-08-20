#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# 链表逆序表示数字


"""
:type l1: ListNode
:type l2: ListNode
:rtype: ListNode
"""
def addTwoNumbers(l1,l2):
    l = ListNode(0)
    result=l
    tmp=0
    while l1 is not None or l2 is not None:
        num1 = 0
        num2 = 0
        if l1 is not None:
            num1=l1.val
            l1=l1.next
        if l2 is not None:
            num2=l2.val
            l2=l2.next
        sum=num1+num2+tmp
        if sum>=10:
            tmp=1
            l.next=ListNode(sum-10)
        else:
            tmp=0
            l.next=ListNode(sum)
        l=l.next
    if tmp==1:
        l.next=ListNode(1)
    return result.next

def addTwoNumbers_2(l1,l2):
    carry=0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1=l1.next
            l1=l1.next
        if l2:
            v2=l2.next
            l2=l2.next
        #divmod返回商和余数的元祖
        carry,val=divmod(v1+v2+carry,10)
        n.next=ListNode(val)
        n=n.next
    return root.next


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    l1=ListNode(5)
    # l1.next=ListNode(4)
    # l1.next.next=ListNode(3)

    l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)

    print addTwoNumbers(l1,l2)
