#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''


def fourSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums) - 3):
        # 第一个数的去重判断
        if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
            tmp_target = target - nums[i]
            for j in range(i + 1, len(nums) - 2):
                # 第二个数的去重判断
                if j == i + 1 or (j > i + 1 and nums[j] != nums[j - 1]):
                    lo, hi = j + 1, len(nums) - 1
                    while lo < hi:
                        if nums[j] + nums[lo] + nums[hi] == tmp_target:
                            result.append([nums[i], nums[j], nums[lo], nums[hi]])
                            while lo < hi and nums[lo] == nums[lo + 1]:
                                lo += 1
                            while lo < hi and nums[hi] == nums[hi - 1]:
                                hi -= 1
                            lo += 1
                            hi -= 1
                        elif nums[j] + nums[lo] + nums[hi] < tmp_target:
                            lo += 1
                        else:
                            hi -= 1
    return result


def fourSum2(nums, target):
    def findNSum(nums, target, N, result, results):
        if len(nums) < N or N < 2 or target < N * nums[0] or target > N * nums[-1]:
            return
        else:
            if N == 2:
                lo, hi = 0, len(nums) - 1
                while lo < hi:
                    if target == nums[lo] + nums[hi]:
                        results.append(result + [nums[lo], nums[hi]])  # 结果列表合并成一个新列表
                        lo += 1
                        while lo<hi and nums[lo]==nums[lo-1]:       # 只需要变一个数就行了
                            lo+=1
                    elif target<nums[lo]+nums[hi]:
                        hi -= 1
                    else:
                        lo += 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        findNSum(nums[i+1:], target - nums[i], N - 1, result + [nums[i]], results)
    nums.sort()
    results = []
    findNSum(nums,target,4,[],results)
    return results

if __name__ == '__main__':
    print fourSum2([-3,-2,-1,0,0,1,2,3],0)
