#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 读excel 使用xlrd模块
def readExcelTest():
    import xlrd
    with xlrd.open_workbook('D://test1.xlsx') as wb:
        sheet = wb.sheets()[0]
        # 获取行数
        nrows = sheet.nrows
        for i in range(nrows):
            print sheet.row_values(i)
    with xlrd.open_workbook('D://test2.xls') as wb:
        sheet = wb.sheet_by_index(0)
        # 按列遍历
        ncols = sheet.ncols
        for i in range(ncols):
            print sheet.col_values(i)
    with xlrd.open_workbook('D://test2.xls') as wb:
        sheet = wb.sheet_by_index(0)
        # 获取单元格内容
        print sheet.row(0)[1].value
        print sheet.cell(0,0).value
        print sheet.cell_value(0,0)
        # ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
        print sheet.cell(0,0).ctype


# 写excel 使用xlwt模块
def writeExcelTest():
    import xlwt
    wb = xlwt.Workbook()
    sheet = wb.add_sheet('sheet1')
    # 单元格写入
    sheet.write(0,1,'aaa')
    # 不支持2007
    wb.save('D://test.xls')

# 用xlrd读取excel 然后用xlutils.copy复制一份才能修改以存在的sheet页
def readWriteTest():
    import xlrd
    from xlutils.copy import copy
    with xlrd.open_workbook('D://test1.xlsx') as wb:
        wb_xls = copy(wb)
        sheet = wb_xls.get_sheet(0)
        sheet.write(5,2,'vvvv')
        wb_xls.save('D://test.xls')


if __name__ == '__main__':
    readExcelTest()
