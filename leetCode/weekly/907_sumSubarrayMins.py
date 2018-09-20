# -*- coding: utf-8 -*-

'''
create by zl on 2018/9/16


Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
'''

def sumSubarrayMins2(A):
    def sumSubarray(A):
        l = len(A)
        if l == 1:
            return A[0]
        else:
            min_val = A[-1]
            sum_min = min_val
            for i in range(l - 2, -1, -1):
                if A[i] < min_val:
                    min_val = A[i]
                sum_min += min_val
        return sum_min
    l = len(A)
    res = 0
    for i in range(1, l + 1):
        res += sumSubarray(A[:i])
    return res % (10**9+7)

'''
1、对每个元素都有可能是某个子数组的最小元素，所以对于某元素，我们可以找出所有的以该元素为最小值的子数组的个数
例如： [3,1,2,4]   以1为最小值的子数组有 [1] [3,1] [3,1,2] [3,1,2,4] [1,2] [1,2,4]总共6个 所以最小值之和 6*1=6
以3为最小值的子数组只有 [3]
2、然后找出每个元素的最小值之和累加起来就是结果所有子数组的最小值之和
3、求以每个元素为最小值的子数组个数，可以为每个i索引处的元素定义(m,n)在A中 A[i]是从A[m]到A[n]中的最小值
例如：[3,1,2,4]中 1在(0,3)中最小，此时子数组个数为  从m到i的长度*从i到n的长度
从m-n范围内都是i处的元素最小  所以取包含i的子数组  向左有i-m+1种取法 向右取有n-i+1种取法
例如：[3,1,2,4]中 i=1 (0,3) m=0 n=3 
'''
def sumSubarrayMins(A):
    l = len(A)
    interval=[[0,0] for _ in range(l)]
    # 先找左边界
    # 栈存放上一个元素的索引 以及上一个元素的m-1索引（即上一个元素一直向左第一个比他小的位置） 以此类推一直到-1
    stack=[-1]
    for i in range(l):
        # 一直向左边找 直到从栈中找到一个比当前元素小的元素
        while stack[-1] != -1 and A[i] < A[stack[-1]]:
            stack.pop()
        # 栈顶是当前元素左边第一个比他小的元素的索引或者-1  所以+1就是能到达的最左边
        interval[i][0] = stack[-1]+1
        # 把当前索引放入栈顶
        stack.append(i)
    # 右边界
    stack = [l]
    for i in range(l-1,-1,-1):
        while stack[-1] != l and A[i] <= A[stack[-1]]:
            stack.pop()
        interval[i][1] = stack[-1] - 1
        stack.append(i)
    res = 0
    for i,v in enumerate(interval):
        m,n = v[0],v[1]
        res += A[i] * (i-m+1) * (n-i+1)
    return res % (10**9+7)

def read_list():
    l=[]
    with open('907','r') as f:
        while 1:
            line = f.readline()
            if not line:
                break
            l.append(int(line))
    return l


if __name__ == '__main__':

    import time
    l=read_list()
    time1 = time.time()
    print(sumSubarrayMins(l))
    time2 = time.time()
    print(time2 - time1)

    print(sumSubarrayMins2(l))
    time3 = time.time()
    print(time3 - time2)