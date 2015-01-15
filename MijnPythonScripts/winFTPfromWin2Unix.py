

 

Combined both suggestions. Final answer being 
#!/usr/bin/python ????
#http://stackoverflow.com/questions/17438096/ftp-upload-files-python
#http://effbot.org/librarybook/ftplib.htm

import ftplib
import os

"""
filename = "MyFile.py"
ftp = ftplib.FTP("xx.xx.xx.xx")
ftp.login("UID", "PSW")
ftp.cwd("/Unix/Folder/where/I/want/to/put/file")
os.chdir(r"\\windows\folder\which\has\file")
myfile = open(filename, 'r')
ftp.storlines('STOR ' + filename, myfile)
myfile.close()
"""

filename = "Replication_201412.xml"
ftp = ftplib.FTP("xx.xx.xx.xx")
ftp.login("kp09nr", "ingJAN15")
ftp.cwd("/appl/summit-nfs/home/kp09nr/temp")
os.chdir(r"\\H:\9_Issue_investigation\JIRA\SUM-10648-ING-LUX-HA-EPIC\SUM-10649\CSVtoXMLscripting\BaseRuns34\ARCH")
myfile = open(filename, 'r')
ftp.storlines('STOR ' + filename, myfile)
myfile.close()
