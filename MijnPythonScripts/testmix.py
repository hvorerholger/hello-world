#testmix bottom-up comprehension of chunks of the xlsx2csv4MM.py script
#

def test1():

    import argparse
    parser = argparse.ArgumentParser(description='convert xlsx File to xml File')
    parser.add_argument("-I", dest="input_file", required=True)
    args = parser.parse_args()

    print (args.input_file)
    xmlFile = args.input_file.replace(".csv",".xml")
    print (xmlFile)

def somethingWithOsPath():
    path = os.path.join(parserObj.sourcedir, parserObj.infile)
    print('path', path)
    print('os.path.split(path)', os.path.split(path))
    print('os.path.basename(path)', os.path.basename(path)) # sequence (path, file)
    print('os.path.dirname(path)', os.path.dirname(path))
    print('os.path.isdir(parserObj.sourcedir)', os.path.isdir(parserObj.sourcedir))
    print('s.path.isfile(path)', os.path.isfile(path))
    print(50*'-')
    """
    #assert os.path.isfile('PROGNOSIS_replication-201401.xlsx')
    """
    
    # absolutePathToInputFile = os.path.join(parserObj.sourcedir, parserObj.infile)
    a = parserObj.infile
    print('a', a)
    temp = os.path.splitext(a)
    print('temp', temp, 'temp[0]', temp[0], 'temp[1]', temp[1] )
    mappedfile = temp[0] + '_PROGNOSIS' + temp[1]
    print('mappedfile', mappedfile)
    absolutePathToMappedFile = os.path.join(parserObj.sourcedir, mappedfile)
    print('absolutePathToMappedFile', absolutePathToMappedFile)
    """
    mappedFile = fName + "_PROGNOSIS"
    shutil.copyfile(absolutePathToInputFile, os.path.join(parserObj.targetdir, mappedFile))
    """

if __name__ == "__main__":
    test1()

