# csv2xml.py
# http://code.activestate.com/recipes/577423-convert-csv-to-xml/
# WVM - 201010107
# First row of the csv file must be header!

# example CSV file: myData.csv
# TradeDate,MMType,Ccy,Start,End,Notional,Index,Rate,Cpty,Company,Desk,Book
# 20140728,DEPOSIT,EUR,20140728,3M,33000000,FIXED,0.02,INTEINT,INGAMS,FXMM,1024DBRU
# 20140728,LOAN,EUR,20140728,20240738,44000000,FIXED,0.02,INTEINT,INGAMS,FXMM,1024DBRU
# 20140728,LOAN,EUR,20140728,20240748,55000000,FIXED,0.02,INTEINT,INGAMS,FXMM,1024DBRU

# v1 operational version for DR
# v2bis = add console based run option functionality with argparse with help usage display
# v3 = add try: except: exception handling for file/ data input
# v4 = add if __name__ == __main__ syntax
# v5 = add comments and docstrings
# v6 = unit tests/ explore unit test modules (no file, file with 0 records, file with only header records, ...)
# check for file permission attributes
# cannot move the *.xml outfile as long as the source file is open in python.exe (IDLE)/ until the shell is closed
# logic mimic almSwapUpload


import argparse, csv, os, sys
    
def parseCmdLineInput():
    print('\n ..parseCmdLineInput')
    # on iMac24 at home
    # sourceDir = '/Users/walter/Documents/GitExercises/hello-world/MijnPythonScripts'
    # targetDir = '/Users/walter/Documents/GitExercises/hello-world/MijnPythonScripts/arch'
    
    # on DellPC at work
    sourceDir = 'H:\9_Issue_investigation\JIRA\SUM-10648-ING-LUX-HA-EPIC\SUM-10923\Baserun_outfiles_ARCH'
    #sourceDir= 'H:\9_Issue_investigation\JIRA\SUM-10648-ING-LUX-HA-EPIC\SUM-10649\CSVtoXMLscripting\BaseRuns34'
    targetDir = 'H:\9_Issue_investigation\JIRA\SUM-10648-ING-LUX-HA-EPIC\SUM-10649\CSVtoXMLscripting\BaseRuns34\ARCH'
    
    parser = argparse.ArgumentParser(description='convert csv File to xml File')
    parser.add_argument("-I", dest="infile", required=True,
                        help='*.csv input file')
    parser.add_argument("-SRC", dest="sourcedir", default=sourceDir,
                        help='XL feed directory')
    parser.add_argument("-DEST", dest="targetdir", default=targetDir,
                        help='outfile directory')
    args = parser.parse_args()
    return args


def processCsv2Xml(fName):
    print('\n ..processCsv2Xml')
    absolutePathToInputFile = os.path.join(parserObj.sourcedir, fName)
    csvData = csv.reader(open(absolutePathToInputFile))
    xmlFile = fName.replace(".csv", ".xml")
    absolutePathToXmlFile = os.path.join(parserObj.targetdir, xmlFile)
    xmlData = open(absolutePathToXmlFile, 'w')
    xmlData.write('<?xml version="1.0"?>' + "\n")
    # there must be only one top-level tag
    xmlData.write('<TRADELIST>' + "\n")

    PorS = 'EMPTY'
    rowNum = 0
    for row in csvData:
        if rowNum == 0:
            tags = row
            # replace spaces w/ underscores in tag names
            for i in range(len(tags)):
                tags[i] = tags[i].replace(' ', '_')
                # print (tags[i])
        else:

            # xmlData.write('<row>' + "\n")
            # for i in range(len(tags)):
            #  xmlData.write('    ' + '<' + tags[i] + '>' \
            #               + row[i] + '</' + tags[i] + '>' + "\n")
            # xmlData.write('</row>' + "\n")

            tags = row
            xmlData.write('   ' + '<MM>' + "\n")
            xmlData.write('   ' + '   ' + '<TradeId/>' + "\n")
            xmlData.write('   ' + '   ' + '<Env SINGLE="Y" TYPE="EntList">' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '<ENV>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<TradeId/>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<Cust>' + tags[8] + '</Cust>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<Company>' + tags[9] + '</Company>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<Desk>' + tags[10] + '</Desk>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<Book>' + tags[11] + '</Book>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '</ENV>' + "\n")
            xmlData.write('   ' + '   ' + '</Env>' + "\n")

            xmlData.write('   ' + '   ' + '<Back SINGLE="Y" TYPE="EntList">' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '<BACK>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<TradeId/>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '</BACK>' + "\n")
            xmlData.write('   ' + '   ' + '</Back>' + "\n")

            xmlData.write('   ' + '   ' + '<Assets SINGLE="N" TYPE="EntList">' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '<ASSET>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<TradeId/>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<Type>MM</Type>' + "\n")

            if tags[1] == 'LOAN':
                PorS = 'P'
            elif tags[1] == 'DEPOSIT':
                PorS = 'S'
            else:
                print ("hello")

            xmlData.write('   ' + '   ' + '   ' + '   ' + '<PorS>' + PorS + '</PorS>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<EffDate>' + tags[3] + '</EffDate>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<MatDate>' + tags[4] + '</MatDate>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<Notional>' + tags[5] + '</Notional>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<Ccy>' + tags[2] + '</Ccy>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<INTEREST_Rate TYPE="Numeric">' + tags[7] + '</INTEREST_Rate>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<INTEREST_dmIndex>' + tags[6] + '</INTEREST_dmIndex>' + "\n")
            xmlData.write('   ' + '   ' + '   ' + '   ' + '<MMType>' + tags[1] + '</MMType>' + "\n")

            xmlData.write('   ' + '   ' + '   ' + '</ASSET>' + "\n")
            xmlData.write('   ' + '   ' + '</Assets>' + "\n")
            xmlData.write('   ' + '</MM>' + "\n")

        rowNum += 1

    xmlData.write('</TRADELIST>' + "\n")
    xmlData.close()


def spielerei():
    pass


def mainloop():
    """
    # --when executing from command line invoking a starting method to pass the cmd line arguments
    parseCmdLineInput()
    print('sys.argv', sys.argv)
    print('sys.argv[2]', sys.argv[2])
    a = parseCmdLineInput()
    print(a.infile)
    print(a.sourcedir)
    print(a.targetdir)
    #processCsv2Xml(sys.argv[2])    #this wont work unless infile exists/resides in cwd (prompt positioning)
    #sys.exit(0)
    
    #--when wanting to Run F5 within IDLE to debug the python script that takes cmd line arguments
    processCsv2Xml('Replication_201410.csv')
    """


if __name__ == '__main__':
    parserObj = parseCmdLineInput()
    processCsv2Xml(parserObj.infile)
