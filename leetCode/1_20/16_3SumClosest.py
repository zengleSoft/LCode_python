#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


def threeSumClosest(nums, target):
    nums.sort()
    sum = nums[0]+nums[1]+nums[len(nums)-1]
    # 三个数之和 与target的间隔
    interval = abs(target - sum)
    for i in range(len(nums) - 2):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            tmp_sum = nums[i] + nums[lo] + nums[hi]
            tmp_interval = abs(target - tmp_sum)
            if target - tmp_sum < 0:
                hi -= 1
            else:
                lo += 1
            if interval > tmp_interval:
                interval = tmp_interval
                sum = tmp_sum
    return sum

if __name__ == '__main__':
    print threeSumClosest([0,0,0],1)