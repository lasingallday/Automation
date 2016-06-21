#Loads C master files by automating UI

import win32com.client
import time
import SendKeys
import os

path = "L:/C_403/toolkit"
os.chdir( path )
shell = win32com.client.Dispatch("WScript.Shell") 

#Open the Toolkit.exe
os.startfile('L:/C_403/toolkit/toolkit.exe')



#Load Fee Master File
time.sleep( 5 )
shell.SendKeys("%t")
time.sleep( 2 )
shell.SendKeys("l")
time.sleep( 2 )
shell.SendKeys("f")
time.sleep( 2 )
shell.SendKeys("{ENTER}")
time.sleep( 2 )
shell.SendKeys("{ENTER}")
time.sleep( 2 )
shell.SendKeys("%x")



#Close the Toolkit.exe
time.sleep( 5 )
shell.SendKeys("%x")
print "Master Files Have Loaded Successfully"