#Loads Cobol zipupdt update file by automating UI

import win32com.client
import time
import SendKeys
import os

path = "L:/Cobol 410"
os.chdir( path )
shell = win32com.client.Dispatch("WScript.Shell") 

time.sleep( 1 )
shell.SendKeys("excload")
time.sleep( 10 )
shell.SendKeys("excrpt")
time.sleep( 10 )
