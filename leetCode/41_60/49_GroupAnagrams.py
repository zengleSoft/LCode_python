#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/3/4

'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: All inputs will be in lower-case.
'''

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tmpDict={}
        for str in strs:
            sList = [s for s in str]
            sList.sort()
            s = ''.join(sList)
            if s in tmpDict:
                tmpDict[s].append(str)
            else:
                tmpDict[s] = [str]
        return tmpDict.values()

if __name__ == '__main__':
    self = Solution()
    print self.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])