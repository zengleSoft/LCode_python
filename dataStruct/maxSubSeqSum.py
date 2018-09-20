#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/4/7

'''
最大子列和问题
给定N各整数序列 {A1,A2,A3...An}
求 子列最大的和
[4,-3,5,-2,-1,2,6,-2]
'''

# 分而治之  先递归求左边最大子列和 在求右边最大子列和 然后求包含中间的最大子列和  比较三个值
def maxSubseqSum3(l,n):
    return divideAndConquer(l,0,n-1)

# 求l从start到end的最大子列和
def divideAndConquer(l,start,end):
    if start==end:
        return l[start] if l[start]>0 else 0
    mid = start + (end-start)//2
    maxLeftSum = divideAndConquer(l,start,mid)
    maxRightSum = divideAndConquer(l,mid+1,end)
    # 找出包含mid的左边最大子列和
    leftSum,tmpLeftSum = 0,0
    for i in range(mid,start-1,-1):
        tmpLeftSum += l[i]
        leftSum = max(leftSum,tmpLeftSum)
    # 找出不包含mid的右边最大子列和
    rightSum,tmpRightSum = 0,0
    for j in range(mid+1,end+1):
        tmpRightSum += l[j]
        rightSum = max(rightSum,tmpRightSum)
    maxMidSum = leftSum + rightSum
    return max(maxLeftSum,maxRightSum,maxMidSum)


# 在线处理方法  子串可以是空
def maxSubseqSum4(l,n):
    if not n:return 0
    thisSum,maxSum = l[0],l[0]
    for i in range(n):
        thisSum += l[i]
        if thisSum>maxSum:
            maxSum = thisSum
        if thisSum<0:
            thisSum = 0
    return maxSum

# 至少包含一个元素
def maxSubseqSum5(l,n):
    if not n:return 0
    maxSum, thisSum = l[0], l[0]
    for i in range(1,n):
        if thisSum < 0 : thisSum=0
        thisSum += l[i]
        if thisSum>maxSum:
            maxSum = thisSum
    return maxSum

if __name__ == '__main__':
    # print (maxSubseqSum4([4,-3,5,-2,-1,2,6,-2],8))
    print (maxSubseqSum5([-3,-2,0,-1],4))
    l = [1,2,3,4,0]
    dp=l[:2]
    print(l[3])
    l[4] = 3