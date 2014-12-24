
import os,csv,calendar,re,decimal,shutil
from openpyxl import load_workbook, Workbook, cell, styles
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-I", dest="input_file", help="input file")
(options, args) = parser.parse_args()

if options.input_file == None:
	print("Input file is not defined. Please run '-h' to get more information.")
	exit()

print (options.input_file)
print (options.input_file)
print (options.input_file[0])

inputFileName_original_ALL = re.findall('Replication.+\.xlsx', options.input_file)
print ('_ALL',inputFileName_original_ALL)

inputFileName_original = re.findall('Replication.+\.xlsx', options.input_file)[0]
print ('[0]:',inputFileName_original)

