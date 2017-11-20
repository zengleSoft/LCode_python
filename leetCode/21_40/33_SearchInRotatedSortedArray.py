#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solutions(object):
    def search(self,nums,target):
        for index,num in enumerate(nums):
            if target == num:
                return index
            if index > 1 and num<nums[index-1] and target<num:
                return -1
        else:
            return -1

    # 二分法
    def search2(self,nums,target):
        if not nums:return -1
        # 先找出数组中最小的元素的索引
        midIndex = self.findMinIndex(nums)

        if target==nums[midIndex]:
            return midIndex

        # 找寻要搜索的上界和下界
        lo = 0 if target>nums[-1] else midIndex
        hi = len(nums)-1 if target<=nums[-1] else midIndex-1

        while lo <= hi:
            mid = lo + (hi-lo)/2
            if nums[mid]==target:return mid
            elif nums[mid]<target: lo=mid+1
            else:hi=mid-1
        return -1

    def findMinIndex(self,nums):
        midIndex, start, end = 0, 0, len(nums) - 1
        while start < end:
            midIndex = start + (end - start) / 2  # midIndex有可能和start一直相等 陷入死循环
            # midIndex要和end比 因为midIndex和end始终不会相等
            if nums[midIndex] > nums[end]:
                start = midIndex + 1
            else:
                end = midIndex
        return start  # 最后循环出来一定是start在正确的位置




if __name__ == '__main__':
    self = Solutions()
    print self.search2([3,1],1)