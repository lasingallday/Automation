#Loads Cobol master files by automating UI

import win32com.client
import time
import SendKeys
import os

path = "L:/Cobol 410"
os.chdir( path )
shell = win32com.client.Dispatch("WScript.Shell") 

time.sleep( 2 )
shell.SendKeys("tax021{ENTER}")
#shell.SendKeys("{ENTER}")
time.sleep( 10 )
shell.SendKeys("zip010{ENTER}")
#shell.SendKeys("{ENTER}")
time.sleep( 20 )
shell.SendKeys("zip080{ENTER}")
#shell.SendKeys("{ENTER}")
time.sleep( 10 )
shell.SendKeys("tax006{ENTER}")
#shell.SendKeys("{ENTER}")
time.sleep( 10 )
shell.SendKeys("excload")
shell.SendKeys("{ENTER}")
time.sleep( 10 )
shell.SendKeys("excrpt")
shell.SendKeys("{ENTER}")
time.sleep( 10 )
