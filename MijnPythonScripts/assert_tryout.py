#--regex tested and validated with PYTHEX.ORG-----------------------------------------------------------------

import re

testDict ={
#positive test cases
't1' : 'replication-201501.xls',      #--lowercase
't2' : 'REPLICATION-201501.xls',      #--uppercase
't3' : 'Replication-201501.xls',      #--mix lowercase uppercase
't4' : 'Replication 201501.xls',      #--datepart preceded by space
't5' : 'Replication_201501.xls',      #--datepart preceded by underscore
't6' : 'Replication-201501.xls',      #--datepart preceded by dash
't7' : 'replication201501.xls',       #--datepart not preceded by space/dash/underscore
't8' : 'replication-201401.xls',      #--datepart abiding lower year boundary
't9' : 'replication-201912.xls',      #--datepart abiding upper year boundary
't10': 'replication_201501.xlsx',     #--Excel stored in Open Office xml format
't11': 'Suivi replication201501.xls', #--filename should contain "replication" in prefixed segment
#negative test cases
't12' : 'Replication_201312.xls',     #--datepart violating lower year boundary 2014
't13' : 'Replication_202001.xls',     #--datepart violating upper year boundary 2019
't14' : 'Replication_201500.xls',     #--datepart not a valid month 
't15' : 'Replication_201513.xls',     #--datepart not a valid month 
't16' : 'Replication_201501.csv',     #--not a valid file extension
't17' : 'Replication_201501brol.xls', #--filename not ending with YYYYMM datepart before extension
}

def validateREfindall(fileName):
    pattern = r'(?P<prefix>[. ]*replication)(?P<delimiter>[_| |-]?)(?P<year>20[1][4-9])(?P<month>0[1-9]|1[0-2])(?P<extension>[.]xlsx?$)'
    result = re.findall(pattern, fileName, re.I)
    print(result) # returns a dictionary with tuples of matched groups, if any                 

def validateREsearch(fileName): 
    pattern = r'(?P<prefix>[. ]*replication)(?P<delimiter>[_| |-]?)(?P<year>20[1][4-9])(?P<month>0[1-9]|1[0-2])(?P<extension>[.]xlsx?$)'
    result = re.search(pattern, fileName, re.I)
    print(result.group(), result.groupdict())
        
if __name__=='__main__':
    for k,v in testDict.items():
        print(k, end=' '), validateREfindall(v)
        
    for k,v in testDict.items():
        try:
            print(k, end=' '), validateREsearch(v)
        except AttributeError:
            print("\t AttributeError: NoneType has no attribute 'group'")
   
    """
    validateREfindall('replication-201501.xls')
    validateREsearch('replication-201501.xls')
    """
    pattern = r'(?P<prefix>[. ]*replication)(?P<delimiter>[_| |-]?)(?P<year>20[1][4-9])(?P<month>0[1-9]|1[0-2])(?P<extension>[.]xlsx$)'
    #positive test case loop
    assert fName = re.findall(pattern, fName, re.I)[0]
    assert re.search(pattern, fName, re.I) is not None
    #negative test case loop
    assert len(re.findall(pattern, fName, re.I) == 0
    assert re.search(pattern, fName, re.I) is None
    

