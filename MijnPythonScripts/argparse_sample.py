# http://argparse.googlecode.com/svn/trunk/doc/add_argument.html#default

import argparse
parser = argparse.ArgumentParser(description='Wordcount some input file')
parser.add_argument("-I", action="store", dest="input_file", required=True)
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
parser.add_argument("-O", action="store", dest="output_file")  #optional - not mandatory
parser.add_argument("-M", "--mode", action="store", dest="mode", help="process mode", choices = ['MTD','YTD'], default='MTD') #default=argpars.SUPPRESS
args = parser.parse_args()

print (args.input_file)
print (args.output_file)
print (args.verbose)
print (args.mode)
if args.verbose:
    print ("verbosity turned on")

file=open(args.input_file,"r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print (k, v)
