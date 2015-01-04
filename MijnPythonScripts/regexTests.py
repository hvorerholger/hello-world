myDict = {'t1' : 'replication-201501.xls',    
't2' : 'REPLICATION-201501.xls',    
't3' : 'Replication-201501.xls',     #--mix lowercase uppercase
't4' : 'Replication 201501.xls',      #--datepart preceded by space
't5' : 'Replication_201501.xls',      #--datepart preceded by underscore
't6' : 'Replication-201501.xls',      #--datepart preceded by dash
't7' : 'replication-201401.xls',      #--datepart abiding lower year boundary
't8' : 'replication-201912.xls',      #--datepart abiding upper year boundary
't9' : 'replication_201501.xlsx',     #--Excel stored in Open Office xml format
#negative test cases
't10' : 'replication201501.xls',      #--datepart not preceded by space/dash/underscore
't11' : 'Replication_201312.xls',     #--datepart violating lower year boundary 2014
't12' : 'Replication_202001.xls',     #--datepart violating upper year boundary 2019
't13' : 'Replication_201500.xls',     #--datepart not a valid month 
't14' : 'Replication_201513.xls',     #--datepart not a valid month 
't15' : 'Replication_201501.csv',     #--not a valid file extension
't16' : 'brolReplication_201501.xls', #--filename not starting with replication
't17' : 'Replication_201501brol.xls', #--filename not ending with YYYYMM datepart before extension
't18' : 'Suivi replication201501.xls'}

import re
m = re.match(r"(?P<int>\d+)\.(\d*)", '3.14')

print (m.lastgroup)
print (m.groups())
print (m.group(0))
print (m.group(1))
print (m.group(2))
print (m.groupdict())
print (m.span())
