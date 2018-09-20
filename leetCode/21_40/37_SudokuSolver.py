#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


'''


class Solution(object):
    def solveSudoku(self, board):
        """
         :type board: List[List[str]]
         :rtype: void Do not return anything, modify board in-place instead.
         """
        self.solve(board)

    def solve(self,board):
        for row_index,row_list in enumerate(board):
            for column_index,val in enumerate(row_list):
                if val=='.':
                    # 从1到9依次试
                    for tmp_val in range(1,10):
                        if self.isvalid(board,row_index,column_index,tmp_val):
                            board[row_index][column_index]=str(tmp_val)
                            # 假设填写正确 递归调用
                            if self.solve(board):
                                return True
                            else:
                                # 如果都不行 回溯
                                board[row_index][column_index]='.'
                    return False
        return True

    # 判断val在row_index和column_index上是否符合数组要求
    def isvalid(self,board,row_index,column_index,val):
        for i in range(9):
            # 检查行
            if board[row_index][i]<>'.' and board[row_index][i]==val:
                return False
            # 检查列
            if board[i][column_index]<>'.' and board[i][column_index]==val:
                return False
            # 检查块
            if board[row_index/3*3 + i/3][column_index/3*3+i%3]<>'.' and board[row_index/3*3 + i/3][column_index/3*3+i%3]==val:
                return False
        return True





    def ifCompete(self,row_dic, column_dic, block_dic,board):
        check_set = set(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        flag = False
        for row_index, row_list in enumerate(board):
            row_dic.setdefault(row_index, set())
            for column_index, val in enumerate(row_list):
                column_dic.setdefault(column_index, set())
                # 根据行、列索引求块索引
                block_index = (row_index / 3) * 3 + column_index / 3
                block_dic.setdefault(block_index, set())
                if val == '.':
                    tmp_set = block_dic.get(block_index) | row_dic.get(row_index) | column_dic.get(column_index)
                    val_set = check_set - tmp_set
                    if len(val_set) == 1:
                        board[row_index][column_index] = val_set.pop()
                    flag = True
                else:
                    row_dic.get(row_index).add(val)
                    column_dic.get(column_index).add(val)
                    block_dic.get(block_index).add(val)
        return flag

if __name__ == '__main__':
    self = Solution()
    self.solveSudoku([[".",".","9","7","4","8",".",".","."],
                      ["7",".",".",".",".",".",".",".","."],
                      [".","2",".","1",".","9",".",".","."],
                      [".",".","7",".",".",".","2","4","."],
                      [".","6","4",".","1",".","5","9","."],
                      [".","9","8",".",".",".","3",".","."],
                      [".",".",".","8",".","3",".","2","."],
                      [".",".",".",".",".",".",".",".","6"],
                      [".",".",".","2","7","5","9",".","."]])
