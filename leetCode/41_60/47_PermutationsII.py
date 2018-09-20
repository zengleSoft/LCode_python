#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/3/3

'''
 Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:

[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

'''

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:return []
        # 利用set去重  set里面只能放不变得元祖
        currentSet = set()
        previousList = [[nums[0]]]
        for num in nums[1:]:
            for l in previousList:
                for i in range(len(l)+1):
                    if i<len(l) and num==l[i]:
                        continue
                    currentSet.add(tuple(l[0:i] + [num] + l[i:]))
            previousList=[list(t) for t in currentSet]
            currentSet=set()
        return previousList

    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:return []
        currentList = []
        previousList = [[nums[0]]]
        for num in nums[1:]:
            for l in previousList:
                for i in range(len(l)+1):
                    currentList.append(l[0:i] + [num] + l[i:])
                    # 对于重复元素 后面总会有重复的结果
                    if i < len(l) and num == l[i]:
                        break
            previousList=[l for l in currentList]
            currentList=[]
        return previousList

if __name__ == '__main__':
    self = Solution()
    print self.permuteUnique2([1,1,2,2])