#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd
import xlwt
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf-8')

def analysis(txtPath):
    res = {}
    file = open(txtPath)
    while 1:
        line = file.readline().strip()
        if not line:
            break
        tmp = line.split(',')
        if tmp[0] in res.keys():
            res.get(tmp[0]).append(int(tmp[1].strip()))
        else:
            res[tmp[0]] = [int(tmp[1].strip())]
    return res

def extractFile(path,fileName,rowNum):
    if fileName.endswith('.xlsx') or fileName.endswith('.xls'):
        with xlrd.open_workbook(path+fileName) as in_excel:
            in_sheet = in_excel.sheet_by_index(0)
            out_excel = xlwt.Workbook()
            out_sheet = out_excel.add_sheet('sheet1')
            for i,row_num in enumerate(rowNum):
                in_row = in_sheet.row_values(row_num)
                for col_num,col in enumerate(in_row):
                    out_sheet.write(i,col_num,col)
        out_excel.save(path+fileName[:fileName.find('.')]+'_extract.xls')
    elif fileName.endswith('.csv'):
        with open(path+fileName,'r') as rf:
            with open(path+fileName[:fileName.find('.')]+'_extract.csv','wb') as wf:
                csv_reader = csv.reader(rf)
                csv_write = csv.writer(wf)
                for row_num,row in enumerate(csv_reader):
                    if row_num in rowNum:
                        csv_write.writerow(row)


if __name__ == '__main__':
    file = analysis('D://test.txt')
    for k,v in file.items():
        extractFile('D://',k,v)
