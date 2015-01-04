
import re, shutil, sys, os, time, datetime
from openpyxl import load_workbook

def valid(file):
    try:
        droplocation = '/Users/walter/Documents/GitExercises/hello-world/MijnPythonScripts'         #*.cfp configparser
        archlocation = '/Users/walter/Documents/GitExercises/hello-world/MijnPythonScripts/arch'
        dropfile = os.path.join(droplocation, file)
        archfile = os.path.join(archlocation, file)
        if not os.path.isfile(dropfile):
            raise FileNotFoundError
        if os.path.isfile(archfile):
            raise RuntimeError
        f = open(fullfile,'r')
        s = f.readline()
    except FileNotFoundError as e:
        print ('File not found in the droplocation:', e)
    except RuntimeError :
        print('File has already been processed // check archive dir', time.strftime('%d/%m/%Y %H:%M:%S', time.gmtime(os.path.getmtime(archfile))))
    except PermissionError as e:
        print ('No read permission on this file:', e)
    else:
        print (s)

def name(myxlsFile):
    foundList = []
    print (re.findall('Replication.+\.xlsx', myxlsFile))
    inputFileName_original = re.findall('Replication.+\.xlsx', myxlsFile)[0]
    print(inputFileName_original)

def kopieer(myxlsFile):
    newxlsFile = 'PROGNOSE_'+myxlsFile
    shutil.copyfile(myxlsFile, newxlsFile)

def checkXL(myxlsFile):
    wb = load_workbook(myxlsFile)
    print(wb.get_sheet_names())
    ws1 = wb['Sheet1']
    ws2 = wb['Sheet2']
    print (ws1.get_highest_row(), ws1.get_highest_column(), ws1.calculate_dimension())
    print(ws1.get_style('E3'))
    print(ws2.calculate_dimension())
    return wb

def date_test(myxlsFile):
    import calendar
    pattern = r'(?P<prefix>[. ]*replication)(?P<delimiter>[_| |-]?)(?P<year>20[1][4-9])(?P<month>0[1-9]|1[0-2])(?P<extension>[.]xlsx$)'
    result = re.search(pattern, myxlsFile, re.I)
    YYYY = result.groupdict()['year']
    print(YYYY)
    MM = result.groupdict()['month']
    print(MM)
    day = calendar.monthrange(int(YYYY),int(MM))[1]  #last day of given month
    mydate = YYYY+MM+"%d" %(day)
    print(day, mydate, type(mydate))
    altYYYYMM = myxlsFile[12:18]
    print(altYYYYMM, type(altYYYYMM))
    

if __name__ == "__main__":
    #valid('TextFile.txt')
    #name('Replication-201501.xlsx')
    #kopieer('Replication-201501.xlsx')
    """
    mywb = checkXL('Replication_201411.xlsx')
    ws1 = mywb['Sheet1']
    assert mywb.get_sheet_by_name('Sheet1') is not None
    assert ws1.get_highest_row() == 11
    assert ws1.get_highest_column() == 88
    assert ws1.calculate_dimension() == "A1:CJ11"
    sheetList =[]
    sheetList = mywb.get_sheet_names()
    for sheet in sheetList:
        ws = mywb[sheet]
        print(sheet, ws.calculate_dimension())
        if sheet == 'Sheet1':
            assert ws.calculate_dimension() == 'A1:A1'
    """
    date_test('Replication_201412.xlsx')
    
 
