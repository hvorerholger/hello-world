import tralala

def assignFormulaToCell():
    wb = load_workbook('Replication_201411.xlsx')
    ws1 = wb['Sheet1']
    _numberFormat = ws1['D3'].number_format

    cell_R17C5 = ws1.cell(row=17, column=5)
    print('ws1.cell(row=3, column=5).coordinate', ws1.cell(row=3, column=5).coordinate)
    print(ws1.cell(row=3, column=5).value)

    print('ws1.cell(row=6, column=5).coordinate', ws1.cell(row=6, column=5).coordinate)
    print(ws1.cell(row=6, column=5).value)

    print('ws1.cell(row9, column=5).coordinate', ws1.cell(row=9, column=5).coordinate)
    print(ws1.cell(row=9, column=5).value)

    cell_R17C5.value = "=SUM(" + ws1.cell(row=3, column=5).coordinate + "," + ws1.cell(row=6, column=5).coordinate + "," + ws1.cell(row=9, column=5).coordinate + ")"
    print ('cell_R17C5.value', type(cell_R17C5.value), cell_R17C5.value, cell_R17C5.internal_value)
    cell_R17C5.number_format = _numberFormat

    cell_R18C5 = ws1.cell(row=18, column=5)
    cell_R18C5.value = ws1.cell(row=3, column=5).value + ws1.cell(row=6, column=5).value + ws1.cell(row=9, column=5).value
    print('ws1.cell_R18C5(row=18, column=5).value', type(ws1.cell(row=18, column=5).value), ws1.cell(row=3, column=5).value)
    print (cell_R18C5.value)
    cell_R18C5.number_format = _numberFormat

    wb.save('Replication_201411_smalltest.xlsx')


def iterateOverCoordinates():
    processing_range = 'E3:CJ11'
    print(processing_range)
    upperleft = (processing_range.partition(':')[0])
    lowerright = (processing_range.partition(':')[2])
    print(upperleft, lowerright)

    xy = coordinate_from_string(upperleft)
    print (xy)
    startcol = column_index_from_string(xy[0])
    print('startcol', startcol)

    xy = coordinate_from_string(lowerright)
    print (xy)
    endcol = column_index_from_string(xy[0])
    print('endcol', endcol)
    maxcol = endcol+1
    print('maxcol', maxcol)

    icol = 5
    print(icol)
    column = get_column_letter(icol)
    print(column)


def defensiveProgramming():
        """
    # considered "too defensive" programming style - remove
    #
    # Sheet1:cellA1 matches up to fname YYYYMM-----#  deze vlieger gaat niet opgaan
    try:
        ws1 = wb['Sheet1']
        c = ws1.cell('A1')
        if c.value is None:
            raise AttributeError
        # to refine
        XLyyyymm = str((c.value.date().year))+str((c.value.date().month))
        if XLyyyymm == fileYYYYMM:
            pass
        else:
            raise RuntimeError
    except AttributeError:
        print('AttributeError: Sheet1:cellA1 is blank')
        raise()
        # to refine
    except RuntimeError:
        print('filecontent cell A1 does not match up with fileName YYYYMM')
        print(c, fileYYYYMM)
        raise()
    else:
        pass
    """


def spielerei(fName):
    pass

def mainloop():
    pass

if __name__ == "__main__":
    mainloop()
