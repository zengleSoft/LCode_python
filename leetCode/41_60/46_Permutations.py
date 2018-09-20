#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/3/3

'''
 Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:

[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

'''


class Solutions(object):
    '''
     先取一个构成结果  [[1]]  然后取下一个元素在上一个结果中list中每个空隙处插入[[2,1],[1,2]]
    '''
    def permute(self, nums):
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
            previousList=[l for l in currentList]
            currentList=[]
        return previousList

    def permute2(self, nums):
        return [[n] + p
                for i, n in enumerate(nums)
                for p in self.permute(nums[:i] + nums[i + 1:])] or [[]]

if __name__ == '__main__':
    self = Solutions()
    print self.permute2([1,2,3])
