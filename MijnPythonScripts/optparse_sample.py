from optparse import OptionParser

parser = OptionParser()
parser.add_option("-I", dest="input_file", help="input file to process")
(options, args) = parser.parse_args()
print (options.input_file)

file=open(options.input_file,"r+")

wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print (k, v)
