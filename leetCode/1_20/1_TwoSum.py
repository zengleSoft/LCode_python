#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


def twoSum(self,nums,target):
    tmp={}
    for i in range(len(nums)):
        if target-nums[i] in tmp:
            return [i,tmp[target-nums[i]]]
        else:
            tmp[nums[i]]=i



if __name__ == '__main__':
    pass
