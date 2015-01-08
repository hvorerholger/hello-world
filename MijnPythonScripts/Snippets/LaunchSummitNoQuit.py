#!H:\bin\python34\python.exe 
import subprocess
import time
import os
import datetime
import shutil
SummitLink='http://acceptance52.summitft.global.intranet/ft_front/dotnet/SummitFT.ATE.application'
#SummitLink='http://sz1201a.itc.intranet/ft_front/dotnet/SummitFT.ATEPRE.application'
#SummitLink='https://devamlony.summit.intranet:8443/ft_front/dotnetsum1/SummitFT.devamlonySUM1.application'

TimeDelay=datetime.timedelta(seconds=10)
MaxTimeDelay=TimeDelay * 2 
CurrentTime=datetime.datetime.now()
TerminateTime=CurrentTime+MaxTimeDelay
subprocess.Popen('C:\Program Files\Internet Explorer\iexplore.exe '+SummitLink)
# #for line in os.popen("tasklist  /FO CSV  /NH /fi \"Imagename eq Summit*\""):
NoInstance=True
ProcessList=[]
while datetime.datetime.now() < TerminateTime and NoInstance:
	lines=os.popen("WMIC process where (Caption like 'Summit%') get CommandLine")
	for line in lines :
		if line.find("No Instance(s) Available.") != -1:
			break
		if (line.find("CommandLine")==-1 and len(line)>2):	
			process=line.replace("\"","").replace("\n","").rstrip()
			ProcessList.append(process)
			NoInstance=False
			print(process)

#---------------restart summit with -NOQUIT option---------------------------#
os.popen("WMIC process where (Caption like 'Summit%') delete")	
time.sleep (3)	
for process in ProcessList: 
#------------------copy correct SummitFT.ATE.exe to the deploy folder-----------#
#------------------temporarily used---------------------------------------------#
	os.popen("copy /Y /B SummitFT.ATE.exe /B "+process)	
	time.sleep (5)			
#--------------------------------------------------------------------------------# 
	process+=" -NOQUIT"	
	subprocess.Popen(process)
	print("==>START: "+process)