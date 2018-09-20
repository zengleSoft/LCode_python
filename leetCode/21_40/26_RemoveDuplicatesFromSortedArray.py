#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
'''

# 返回不重复长度 并且原始数组前面的都不是重复的
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return
        res = 0
        for i in range(1,len(nums)):
            if nums[res]<>nums[i]:
                nums[res] = nums[i]
                res += 1
        return res+1
