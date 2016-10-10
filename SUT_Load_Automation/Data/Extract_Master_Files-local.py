#Loads C master files by automating UI

import win32com.client
import time
import SendKeys
import subprocess
from datetime import datetime

#startTime = datetime.now()
shell = win32com.client.Dispatch("WScript.Shell") 
currentYear = "2016"
priorMonth = "02"
#extractFolder = "'//Corp.sovos.local/WIL/Departments/TaxContentQA/Test Artifacts & Results/Special_Projects/SUT Automation/Template/Files/Prod/Main/Cobol'"
system = []
system.append("cobol")
system.append("c")
system.append("plsql")
filenameString = []

for i in range(0,3):
	filenameString.append("7z x " + "C:/Users/jeffrey.thomas/Downloads/" + currentYear + "-" + priorMonth + "-sut-" + system[i] + "-regular-full.zip")
	print(filenameString[i])

#Load the Tax Master File
shell.SendKeys(filenameString[0])
shell.SendKeys("{ENTER}")
time.sleep(10)
shell.SendKeys(filenameString[1])
shell.SendKeys("{ENTER}")
time.sleep(10)
shell.SendKeys(filenameString[2])
shell.SendKeys("{ENTER}")

print "Master Files Have Unzipped Successfully"
#print datetime.now() - startTime

time.sleep(20)
subprocess.call('move /y 2016-02-sut-cobol-regular-full\MainFiles\* "T:\WIL\Departments\TaxContentQA\Test Artifacts & Results\Special_Projects\SUT Automation\Template\Files\Prod\Main\Cobol"',shell=True)
subprocess.call('copy 2016-02-sut-c-regular-full\MainFiles\zipseq "T:\WIL\Departments\TaxContentQA\Test Artifacts & Results\Special_Projects\SUT Automation\Template\Files\Prod\Main\PLSQL"',shell=True)
subprocess.call('move /y 2016-02-sut-c-regular-full\MainFiles\* "T:\WIL\Departments\TaxContentQA\Test Artifacts & Results\Special_Projects\SUT Automation\Template\Files\Prod\Main\C"',shell=True)
subprocess.call('move /y 2016-02-sut-plsql-regular-full\MainFiles\* "T:\WIL\Departments\TaxContentQA\Test Artifacts & Results\Special_Projects\SUT Automation\Template\Files\Prod\Main\PLSQL"',shell=True)
