#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/1/14

'''
[[1,10],[2,3],[5,8],[4,7]]
找出最多共有区间的个数   [1,10],[5,8],[4,7]
return 3
'''

def intervalTest(list,start,end):
    if start>=end:return list
    begin,finish=start,end
    key = list[start][0]
    while begin<finish:
        while begin<finish and key<=list[finish][0]:
            finish-=1
        while begin<finish and list[begin][0]<=key:
            begin+=1
        if begin<finish:
            list[begin],list[finish]=list[finish],list[begin]
    list[start],list[begin] = list[begin],list[start]
    intervalTest(list,start,begin-1)
    intervalTest(list,begin+1,end)
    return list


if __name__ == '__main__':
    list = [[1,10],[2,3],[5,8],[4,7]]
    intervalTest(list,0,3)
    tmp_result,result = 0,0
    left,right = list[0][0],list[0],[1]
    for l in list:
        if l[0]>right:
            left,right=l[0],l[1]
            tmp_result=1
            continue
        elif l[0]<=right:
            left = l[0]
            tmp_result+=1

