#Loads C master files by automating UI

import win32com.client
import time
import SendKeys
import subprocess
from datetime import datetime
from varfile import currentYear, currentNoMonth, buildTypePartialPath

#startTime = datetime.now()
shell = win32com.client.Dispatch("WScript.Shell")
#extractFolder = "'T:\WIL\Departments\TaxContentQA\Test Artifacts & Results\Special_Projects\SUT Automation\Template'"
system = ["cobol", "c", "plsql"]
zipType = ["full", "incremental"]
filenameString = []

for i in range(0,2):
	for j in range(0,3):
		filenameString.append("7z x " + "C:/Users/jeffrey.thomas/Downloads/" + currentYear + "-" + currentNoMonth + "-sut-" + system[j] + "-" + buildTypePartialPath + "-" + zipType[i] + ".zip")
		print(filenameString[j])

#Unzip the Tax Master File
for k in range(0,6):
	shell.SendKeys(filenameString[k])
	shell.SendKeys("{ENTER}")
	time.sleep(10)

print "Master Files Have Unzipped Successfully"
#print datetime.now() - startTime
