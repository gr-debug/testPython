__author__='gr'
# -- coding:utf-8 --
#!/usr/bin/python3
import numpy as np
import xlrd
from datetime import date,datetime
file = 'C:\PythonMyApp\HTZQ20191125.xlsx'
def read_excel():
    wb = xlrd.open_workbook(filename=file)
    print(wb.sheet_names())

    sheet1 = wb.sheet_by_index(0)   #通过索引获取表格
    sheet2 = wb.sheet_by_name('gz_zg') #通过名字获取表格
    # print(sheet1,sheet2)
    # print(sheet1.name,sheet1.nrows,sheet1.ncols)
    rows = sheet1.row_values(2) #获取行内容
    cols = sheet1.col_values(3) #获取列内容
    print(rows)
    print(cols)



read_excel()









