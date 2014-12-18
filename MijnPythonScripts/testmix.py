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



if __name__ == "__main__":
    test1()

