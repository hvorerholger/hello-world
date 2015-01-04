import argparse,calendar,csv,decimal,os,re,shutil,time
from openpyxl import load_workbook, Workbook, cell, styles


def archtest(fName):  
    archivedir  = '/Users/walter/Documents/GitExercises/hello-world/MijnPythonScripts/arch'   #*.cfp configparser or cmdLine default
    os.chdir(archivedir)
    archList=os.listdir(archivedir)
    for file in archList:
        archfileYYYYMM = ''
        try:
            match = re.search(pattern, file, re.I)
            if match == None:
                continue
            else:
                archfileYYYYMM = match.groupdict()['year']+match.groupdict()['month']
                if archfileYYYYMM == fileYYYYMM:
                    raise RuntimeError
        except RuntimeError:
            print('in archive dir exist file(s) already processed for period YYYY MM: ', fileYYYYMM, file, \
                  time.strftime('%d/%m/%Y %H:%M:%S', time.gmtime(os.path.getmtime(file))))
            raise
        else:
            pass

if __name__ == "__main__":

    archtest('Replication_201412.xls')
