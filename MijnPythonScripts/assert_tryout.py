import re
#--testcases------------------------------------------------------------------------------------
#--regex tested with pythex.org-----------------------------------------------------------------
#--should test positive
t1 = 'replication-201501.csv'      #--lowercase
t2 = 'REPLICATION-201501.CSV'      #--uppercase
t3 = 'Replication-201501.csv'      #--mix lowercase uppercase
t4 = 'Replication 201501.csv'      #--datepart preceded by space
t5 = 'Replication_201501.csv'      #--datepart preceded by underscore
t6 = 'Replication-201501.csv'      #--datepart preceded by dash
t7 = 'replication-201401.csv'      #--datepart abiding lower year boundary
t8 = 'replication-201912.csv'      #--datepart abiding upper year boundary
#--start of negative tests
t9 = 'Suivi replication201501.csv' #--filename should start with "replication"(IGNORECASE)
t10 = 'replication201501.csv'      #--datepart not preceded by space/dash/underscore
t11 = 'Replication_201312.csv'     #--datepart violating lower year boundary 2014
t12 = 'Replication_202001.csv'     #--datepart violating upper year boundary 2019
t13 = 'Replication_201500.csv'     #--datepart not a valid month 
t14 = 'Replication_201513.csv'     #--datepart not a valid month 
t15 = 'Replication_201501.xls'     #--not a valid file extension
t16 = 'brolReplication_201501.xls' #--filename not starting with replication
t17 = 'Replication_201501brol.csv' #--filename not ending with YYYYMM datepart before extension
#--loop thru list
testlist = [t1,t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15, t16, t17]

def validFileName(myFileName):
    try:
        assert (re.search\          #pattern
                (r'(?P<prefix>^replication)(?P<delimiter>[\s|_|-])(?P<year>20[1][4-9])(?P<month>0[1-9]|1[0-2])(?P<extension>[.]csv$)',\ 
                 myFileName,\       #in string
                 re.IGNORECASE))\   #with flags
                 is not None
        
    except AssertionError:
        #print ('Invalid FileNamePattern: ', myFileName, '\t', 'expecting: replication_YYYYMM.csv') # gaat dit naar stdout?
        return False
    else:
        #searchObj = re.search(r'(?P<prefix>^replication)(?P<delimiter>[\s|_|-])(?P<year>20[1][4-9])(?P<month>0[1-9]|1[0-2])(?P<extension>[.]csv$)', myFileName, re.IGNORECASE)
        #print ('BINGO! valid filename: ', '\t ', myFileName, '\t', 'datepart: ', datepart, '\t','year: ',searchObj.group('year'),'   month: ',searchObj.group('month'))
        return True

if __name__=='__main__':
    for test in testlist:
        datepart = test[12:18]
        #validFileName(test)
        """if validFileName(test):
            print ('BINGO')"""
        if validFileName(test):
            print (test,'BINGO!')
        





        
        
