import argparse

parser = argparse.ArgumentParser(description='Process some input file')

parser.add_argument("-I", action="store", dest="input_file")
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity") 

args = parser.parse_args()

print (args.input_file)
print (args.verbose)

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
