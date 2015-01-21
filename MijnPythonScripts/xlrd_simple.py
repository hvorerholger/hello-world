#! /usr/bin/env python

from mmap import mmap,ACCESS_READ
from xlrd import open_workbook


def openingWorkbook(fName):
    from mmap import mmap,ACCESS_READ
    from xlrd import open_workbook
    print (open_workbook(fName))
    with open(fName, 'rb') as f:
        print (open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ)))
    aString = open(fName,'rb').read()
    print (open_workbook(file_contents=aString))


def navigatingWorkbook(fName):
    wb = open_workbook(fName)
    for s in wb.sheets():
        print ('Sheet:',s.name)
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                values.append(str(s.cell(row,col).value))   #str instances expected
            print (','.join(values))
        print


def introspectWorkbook(fName):
    from xlrd import open_workbook
    book = open_workbook(fName)
    print(book.nsheets)
    for sheet_index in range(book.nsheets):
        print (book.sheet_by_index(sheet_index))
    print (book.sheet_names())
    for sheet_name in book.sheet_names():
        print (book.sheet_by_name(sheet_name))
    for sheet in book.sheets():
        print (sheet)


def introspectSheet(fName):
    from xlrd import open_workbook,cellname
    book = open_workbook(fName)
    sheet = book.sheet_by_index(0)
    print (sheet.name)
    print (sheet.nrows)
    print (sheet.ncols)
    for row_index in range(sheet.nrows):
        for col_index in range(sheet.ncols):
            print (cellname(row_index,col_index),'-',)
            print (sheet.cell(row_index,col_index).value)


def cellAccess():
    from xlrd import open_workbook,XL_CELL_TEXT
    
    book = open_workbook('simple.xlsx')
    sheet = book.sheet_by_index(1)
    cell = sheet.cell(3,1)
    print (cell)
    print (cell.value)
    print (cell.ctype==XL_CELL_TEXT)
    for i in range(sheet.ncols):
        print (sheet.cell_type(1,i),sheet.cell_value(1,i))

def utility():
    from xlrd import cellname, cellnameabs, colname
    print (cellname(0,0),cellname(10,10),cellname(100,100))
    print (cellnameabs(3,1),cellnameabs(41,59),cellnameabs(265,358))
    print (colname(0),colname(10),colname(100))

    

if __name__ == "__main__":
    #openingWorkbook('simple.xlsx')
    navigatingWorkbook('simple.xlsx')
    #introspectWorkbook('simple.xlsx')
    #introspectSheet('simple.xlsx')
    #cellAccess()
