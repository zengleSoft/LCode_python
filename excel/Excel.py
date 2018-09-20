#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlwt
import xlrd

def copyRow():
    data = xlrd.open_workbook('D://telephone.xlsx')
    table = data.sheet_by_index(0)
    nrows = table.nrows
    file = xlwt.Workbook(encoding='utf-8',style_compression=0)
    sheet = file.add_sheet('data')

    line = table.row_values(0)
    col = 0
    for i in line:
        sheet.row(0).write(col,i)
        col += 1
    file.save('D://copy.xls')







if __name__ == '__main__':
    copyRow()