#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
import xlwt
import sys
import pandas
reload(sys)
sys.setdefaultencoding('utf-8')

def analysis(txtPath):
    res = {}
    file = open(txtPath)
    while 1:
        line = file.readline()
        if not line:
            break
        tmp = line.split(',')
        if tmp[0] in res.keys():
            res.get(tmp[0]).append(int(tmp[1].strip()))
        else:
            res[tmp[0]] = []
    return res

def extractFile(path,fileName,rowNum):
    if fileName.endswith('.xlsx'):
        in_excel = xlrd.open_workbook(path+fileName)
        out_excel = xlwt.Workbook()
        out_sheet = out_excel.add_sheet()
        in_sheet = in_excel.sheet_by_index(0)
        for i in rowNum:
            in_row = in_sheet.row_values(i)
            out_sheet.write(in_row)




    elif fileName.endswith('.csv'):
        print 2


if __name__ == '__main__':
    file = analysis('D://ym.txt')
    for k,v in file.items():
        extractFile('',k,v)
