#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/7/12
class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_dict = {}
        self.random_list = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.random_dict:
            return False
        else:
            self.random_list.append(val)
            self.random_dict[val] = len(self.random_list) - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.random_dict:
            i = self.random_dict[val]
            self.random_list[i], self.random_list[-1] = self.random_list[-1], self.random_list[i]
            self.random_list.pop()
            self.random_dict.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.random_list:
            import random
            i = random.randint(0, len(self.random_list) - 1)
            return self.random_list[i]


def mySqrt(x):
    start, end, cur = 0, x, x
    while cur > 0:
        tmp = cur ** 2
        if tmp > x:
            end = cur
        elif tmp == x:
            return int(cur)
        else:
            start = cur
        cur2 = start + (end - start) / 2
        if cur != cur2 and int(cur) == int(cur2):
            return int(cur2)
        else:
            cur = cur2
    return x

if __name__ == '__main__':
    print(mySqrt(5))