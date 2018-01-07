#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''


class Solutions(object):
    def searchRange(self, nums, target):
        i, j = 0, len(nums) - 1
        start,end=-1,-1
        # 先找第一个target
        while i <= j:
            mid = i + (j - i) / 2
            if nums[mid] == target:
                if mid > 0 and nums[mid - 1] == target:
                    j = mid - 1
                else:
                    start = mid
                    break
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        if start==-1:return [-1,-1]
        i,j=start,len(nums)-1
        # 再找最后一个target
        while i <= j:
            mid = i + (j - i) / 2
            if nums[mid] == target:
                if mid < len(nums)-1 and nums[mid + 1] == target:
                    i = mid + 1
                else:
                    end = mid
                    break
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return [start,end]

    def searchRange2(self, nums, target):
        i, j = 0, len(nums) - 1
        start,end=-1,-1
        # 先找第一个target
        while i <= j:
            mid = i + (j - i) / 2
            if nums[mid]==target and (mid==0 or nums[mid-1]<>target):
                start = mid
                break
            elif nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        if start==-1:return [-1,-1]
        i,j=start,len(nums)-1
        # 再找最后一个target
        while i <= j:
            mid = i + (j - i) / 2
            if nums[mid]==target and (mid==len(nums)-1 or nums[mid+1]<>target):
                end = mid
                break
            elif nums[mid]>target:
                j = mid-1
            else:
                i = mid+1
        return [start,end]

if __name__ == '__main__':
    self = Solutions()
    print self.searchRange2([2,2],2)