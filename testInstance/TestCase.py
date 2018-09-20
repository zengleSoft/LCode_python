#!/usr/bin/python
# -*- coding: UTF-8 -*-

def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums: return 0
    if len(nums) < 3:
        return max(nums[0], nums[-1])
    dp = nums
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[-1]


class MinStack:
    dataStack = []
    minStack = []

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dataStack = []
        self.minStack = []  # 栈顶始终记录当前栈长度的最小值，长度和数据栈长度保持一致

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.dataStack.append(x)
        if self.minStack:
            self.minStack.append(min(self.minStack[-1], x))
        else:
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.minStack:
            self.minStack.pop()
        if self.dataStack:
            return self.dataStack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.dataStack:
            return self.dataStack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]


def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    row = set()
    col = set()
    for rowIndex, l in enumerate(matrix):
        for colIndex, val in enumerate(l):
            if val == 0:
                row.add(rowIndex)
                col.add(colIndex)
    for rowIndex, l in enumerate(matrix):
        if rowIndex in row:
            matrix[rowIndex] = [0 for _ in matrix[0]]
        else:
            for colIndex, val in enumerate(l):
                if colIndex in col:
                    matrix[rowIndex][colIndex] = 0


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s: return 0
    maxs, tmps = s[0], s[0]
    for i in s[1:]:
        if i not in tmps:
            tmps += i
        else:
            if len(maxs) < len(tmps):
                maxs = tmps
            index = tmps.find(i)
            tmps = tmps[index + 1:] + i

    return max(len(maxs), len(tmps))


def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    maxNum= max(nums)+1
    minNum,secNum = maxNum,maxNum
    for num in nums:
        if minNum>=num:minNum=num
        elif secNum>=num:secNum=num
        else:return True
    return False




if __name__ == '__main__':
    print(increasingTriplet([1,2,-10,-8,-7]))