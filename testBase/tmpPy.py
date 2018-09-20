#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/3/11

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if not intervals: return []

    def quickSort(intervals, start, end):
        if start >= end: return
        left, right = start, end
        target = intervals[start].start
        while left < right:
            while left < right and intervals[right].start >= target:
                right -= 1
            while left < right and intervals[left].start <= target:
                left += 1
            intervals[left], intervals[right] = intervals[right], intervals[left]
        intervals[left], intervals[start] = intervals[start], intervals[left]
        quickSort(intervals, start, left - 1)
        quickSort(intervals, left + 1, end)

    quickSort(intervals, 0, len(intervals) - 1)
    res, tmp = [], intervals[0]
    for i in intervals[1:]:
        if i.start <= tmp.end:
            tmp.end = i.end
        else:
            res.append(tmp)
            tmp = i
    res.append(tmp)


def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    minIndex = findMinIndex(nums)
    if nums[minIndex] == target: return minIndex
    start = minIndex if nums[-1] >= target else 0
    end = minIndex - 1 if nums[-1] < target else len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


def findMinIndex(nums):
    start, end = 0, len(nums) - 1
    while start < end:
        mid = start + (end - start) // 2
        if nums[mid] < nums[end]:
            end = mid
        else:
            start = mid + 1
    return start


def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    minCoin = min(coins)
    dp = [-1 for _ in range(amount + 1)]
    dp[0] = 0
    for i in range(minCoin, amount + 1):
        tmp = -1
        for j in coins:
            if i >= j and dp[i - j] > -1:
                tmp = min(dp[i - j] + 1, tmp) if tmp > -1 else dp[i - j] + 1
        dp[i] = tmp
    return dp[-1]


def coinChange2(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [0] + [-1] * amount
    for i in range(amount):
        if dp[i] < 0:
            continue
        for j in coins:
            if j + i > amount:
                continue
            if dp[i + j] < 0 or dp[i + j] > dp[i] + 1:
                dp[i + j] = dp[i] + 1
    return dp[-1]


def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 有序数组  维护一个
    if not nums: return 1
    tmp = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > tmp[-1]:
            tmp.append(nums[i])
        elif nums[i] < tmp[0]:
            tmp[0] = nums[i]
        else:
            # 在tmp有序数组中找第一个大于nums[i]的位置
            start, end = 0, len(tmp) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if tmp[mid] < nums[i]:
                    start = mid + 1
                elif tmp[mid] > nums[i]:
                    end = mid - 1
                else:
                    start = mid
                    break
            tmp[start] = nums[i]
    return len(tmp)


def get_partial_match_table(s):
    prefix = set()
    res = [0]
    for i in range(1, len(s)):
        prefix.add(s[:i])
        postfix = {s[j:i + 1] for j in range(1, i + 1)}
        res.append(len((prefix & postfix or {''}).pop()))
    return res


def kmp(pat, txt):
    m, n = len(pat), len(txt)
    cur = 0
    t = get_partial_match_table(pat)
    while cur < n - m:
        for i in range(m):
            if txt[i + cur] != pat[i]:
                cur += max(i - t[i - 1], 1)
                break
        else:
            return cur
    return -1


def get_right_dict(s):
    d = {}
    for i in range(len(s) - 1, -1, -1):
        if s[i] not in d:
            d[s[i]] = i
    return d


def bm(pat, txt):
    m, n = len(pat), len(txt)
    d = get_right_dict(pat)
    cur = 0
    while cur <= n - m:
        for i in range(m - 1, -1, -1):
            if txt[i + cur] != pat[i]:
                j = d[txt[i + cur]] if txt[i + cur] in d else -1
                cur += max(i - j, 1)
                break
        else:
            return cur
    return -1


# 将不符合堆结构的元素下沉到合适的位置
def sink(nums, i, n):
    while i < n:
        j = 2 * i + 1
        # 选出左右孩子中较大的
        if j < n - 1 and nums[j] < nums[j + 1]:
            j += 1
        if j < n and nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i = j
        else:
            break

def sort(nums):
    n = len(nums)
    # 构造大顶堆
    for i in range(n // 2 - 1, -1, -1):
        sink(nums, i, n)
    for j in range(n - 1):
        n -= 1
        nums[0], nums[n] = nums[n], nums[0]
        sink(nums, 0, n)

# 将不符合堆结构的元素下沉到合适的位置
def sink(nums, i, n):
    while i < n:
        j = 2 * i + 1
        # 选出左右孩子中较大的
        if j < n - 1 and nums[j] < nums[j + 1]:
            j += 1
        if j < n and nums[i] < nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i = j
        else:
            break

def sort(nums):
    n = len(nums)
    # 构造大顶堆
    for i in range(n // 2 - 1, -1, -1):
        sink(nums, i, n)
    for j in range(n - 1):
        n -= 1
        nums[0], nums[n] = nums[n], nums[0]
        sink(nums, 0, n)

def rotate(l,i):
    n = len(l)
    for j in range(i):
        tmp = l[j]
        while j < n-i:
            l[j] = l[j+i]
            j += i
        l[j] = tmp


if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9]
    rotate(l,2)
    print(l)