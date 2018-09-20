#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
'''

"""
:type board: List[List[str]]
:rtype: bool
"""
class Solution(object):
    def isValidSudoku(self,board):
        # 行、列、快 字典存储 索引和元素
        line_dic,column_dic,block_dic={},{},{}
        for line_index,line_list in enumerate(board):
            if line_index<3:
                block_indexs=[0,1,2]
            elif line_index<6:
                block_indexs=[3,4,5]
            else:
                block_indexs=[6,7,8]
            # 初始化行dic
            line_dic.setdefault(line_index,set())
            for column_index,val in enumerate(line_list):
                # 初始化列dic
                column_dic.setdefault(column_index,set())
                # 初始化块dic  根据行、列索引计算块索引
                if column_index<3:
                    block_index=block_indexs[0]
                elif column_index<6:
                    block_index=block_indexs[1]
                else:
                    block_index=block_indexs[2]
                block_dic.setdefault(block_index,set())
                #判断行和列
                if val!='.' and (val in line_dic.get(line_index) or val in column_dic.get(column_index) or val in block_dic.get(block_index)):
                    return False
                line_dic.get(line_index).add(val)
                column_dic.get(column_index).add(val)
                block_dic.get(block_index).add(val)
        return True

    def isValidSudoku2(self,board):
        for i in range(9):
            row_set,column_set,block_set=set(),set(),set()
            for j in range(9):
                # 检查行
                if board[i][j]!='.' and board[i][j] in row_set:
                    return False
                else: row_set.add(board[i][j])
                #检查列
                if board[j][i]!='.' and board[j][i] in column_set:
                    return False
                else: column_set.add(board[j][i])
                # 检查块
                row_index = 3*(i//3)
                column_index = 3*(i%3)
                if board[row_index + j//3][column_index + j%3]!='.' and board[row_index + j//3][column_index + j%3] in block_set:
                    return False
                else : block_set.add(board[row_index + j//3][column_index + j%3])
        return True





if __name__ == '__main__':
    self = Solution()
    print (self.isValidSudoku([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]))