import os,re

def validateInputFile(fileName):
    """    #valid name, file exists in importdir, >0Kb, readable, content-checks, duplicate processing check
    #valid file name---------------------------#
    pattern = r'(?P<prefix>[. ]*replication)(?P<delimiter>[_| |-]?)(?P<year>20[1][4-9])(?P<month>0[1-9]|1[0-2])(?P<extension>[.]xlsx?$)'
    result = re.search(pattern, fileName, re.I)
    try:
        if result == None:
            raise RuntimeError
    except RuntimeError:
        print ('Not a valid filename:', fileName, 'Expecting: *replication*YYYYMM.xls(x)') #cannot provide result.group() and .groupdict()
        raise
    else:
        pass
"""
    #file does not exist in archive dir-------#
    archivedir  = '/Users/walter/Documents/GitExercises/hello-world/MijnPythonScripts/arch'   #*.cfp configparser or cmdLine default
    absolutizedArchiveFile  = os.path.join(archivedir, fileName)
    try:
        if os.path.isfile(absolutizedArchiveFile):  #expand logic to scan archive directory if exist files with corresponding YYYYMM 
            raise RuntimeError
    except RuntimeError:
        print('a file has already been processed for YYYY MM // check archive dir')
        lastmod = os.path.getmtime(absolutizedArchiveFile)
        lastmodFormatted = time.strftime('%d/%m/%Y %H:%M:%S', time.gmtime(lastmod))
        print(lastmodFormatted)
    else:
        pass

    #file exists in droplocation--------------#
    droplocation  = '/Users/walter/Documents/GitExercises/hello-world/MijnPythonScripts'   #*.cfp configparser or cmdLine default
    absolutizedImportFile  = os.path.join(droplocation, fileName)
    try:
        if not os.path.isfile(absolutizedImportFile):
            raise FileNotFoundError
    except FileNotFoundError as e:
        print ('File not found in the drop location:', e)
        raise



    #file name matches expected file content-----------#
    #<year><month> in file name should correspond to cell A1 content
    #Sheet1 range A1 - XXnn containing monthly replication profile

if __name__ == '__main__':
    validateInputFile('TestFile.txt')
