infile = 'replication_201501.csv'
import re
"""#assert ((infile.startswith('Replication')==True and (infile.endswith('.csv')==True)
"""

if re.search(r"^replication[_|-](20[1-2][0-9](0[1-9]|1[0-2].csv$))", infile, re.IGNORECASE):
         print ('success')
else:
         print ("Expecting a file named 'Replication_yyyymm.csv'")

#assertIsNotNone (re.search(r"^replication[_|-](20[1-2][0-9](0[1-9]|1[0-2].csv$))", infile, re.IGNORECASE))

s = re.search(r"^replication[_|-](20[1-2][0-9](0[1-9]|1[0-2].csv$))", infile, re.IGNORECASE)
print (type(s))

"""

if re.search(r"^[Rr]eplication_", infile) and re.search(r".csv$", infile):
         print ('success')
else:
         print ("Expecting a file named 'Replication_yyyymm.csv'")
"""
"""
if (infile.startswith ('Replication_') and  (infile.endswith('.csv'))):
         print ('success')
else:
         print ("Expecting a file named 'Replication_yyyymm.csv'")
  
print (infile[12:18])

def datepart_from_filename (datepart):
    m= re.match(".*(?P<YEAR>[0-9]{4})(?P<MONTH>[0-9]{2}).csv", filename)
    year = int(m.group('YEAR'))
    month = int(m.group('MONTH'))
    print (year)
    pring (month)

def validFileName (filename):
    fn = filename
    if (fn.startswith('Replication') and
        fn.endswith('.csv') and
        fn[12:18] == 201501):
        return True
    else:
        print ("not a valid filename, expecting 'Replication_YYYYMM.csv'")
"""



        
        
