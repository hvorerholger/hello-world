#tested in http://pythex.org/

import re
infile = 'replication 201501.csv'
searchObj = re.search(r'(?P<prefix>^replication)(?P<delimiter>[\s|_|-])(?P<year>20[1][4-9])(?P<month>0[1-9]|1[0-2])(?P<extension>[.]csv$)', infile, re.IGNORECASE)

print (searchObj.group('year'))
print (searchObj.group('month'))
