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


def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    flag = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
    dividend, tmp_divisor, divisor = abs(dividend), abs(divisor), abs(divisor)
    res = 0
    span = 1
    while dividend >= divisor or span > 1:
        if tmp_divisor > dividend:
            tmp_divisor -= divisor
            span -= 1
            continue
        dividend -= tmp_divisor
        res += span
        tmp_divisor += divisor
        span += 1
    res = res if flag > 0 else -res
    return res

if __name__ == '__main__':
    print(divide(-2147483648,-1))