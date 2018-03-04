#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 2018/3/3

'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

'''
'''
/*
 * clockwise rotate  上下翻转  让后对角线翻转
 * first reverse up to down, then swap the symmetry
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
'''

class Solution(object):
    #
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 一圈一圈的交换
        for i in range(n/2):
            # 先交换顶点  定义顶点位置
            matrix[i][i], matrix[i][n - i - 1 ], matrix[n - i  - 1 ][n - i  - 1 ], matrix[n - i  - 1 ][i] \
                = matrix[n - i  - 1 ][i],matrix[i][i], matrix[i][n - i  - 1 ], matrix[n -i  - 1 ][n - i  - 1 ]
            # 循环交换边上的点  根据顶点位置相应变化
            for j in range(1,n-2*i-1):
                matrix[i][i + j], matrix[i+j][n - i - 1], matrix[n - i - 1][n - i - 1 - j], matrix[n - i - 1 - j][i] \
                    = matrix[n - i - 1 - j][i],matrix[i][i + j], matrix[i+j][n - i - 1], matrix[n - i - 1][n - i - 1 - j]

    def rotate2(self, matrix):
        '''         [::-1]      zip()           zip(*)
         1 2 3      7 8 9       ((7,8,9),)      7 4 1
         4 5 6  --> 4 5 6   --> ((4,5,6),) -->  8 5 2
         7 8 9      1 2 3       ((1,2,3),)      9 6 3
        :param matrix:
        :return:
        '''
        matrix[::] = zip(*matrix[::-1])

if __name__ == '__main__':
    matrix = [
  [ 1,2,3],
  [ 4,5,6],
  [7,8,9],
]
    # self = Solution()
    # self.rotate2(matrix)
    print matrix[::-1]
    print zip(matrix[::-1])