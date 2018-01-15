#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/1/8


'''
 Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.
从1开始找 找到了在找2...

Your algorithm should run in O(n) time and uses constant space.
利用数组索引记录  将数组正序交换
'''

class Solution(object):
    def firstMissingPositive(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index=0
        while index < len(nums):
            # 当元素在索引长度范围并且不等于要交换位置的元素
            if nums[index] > 0 and nums[index]<len(nums)+1 and nums[nums[index] - 1]<>nums[index]:
                nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
                continue
            index += 1
        for index,val in enumerate(nums):
            if index+1<>val:
                return index+1
        else:return len(nums)+1




if __name__ == '__main__':
    self = Solution()
    print self.firstMissingPositive([1,1])