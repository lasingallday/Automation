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


#Load the Exception File
time.sleep( 5 )
SendKeys.SendKeys("%t")
time.sleep( 1 )
SendKeys.SendKeys("l")
time.sleep( 1 )
SendKeys.SendKeys("e")
time.sleep( 1 )
SendKeys.SendKeys("%r")
time.sleep( 1 )
SendKeys.SendKeys("{ENTER}")
time.sleep( 1 )
SendKeys.SendKeys("%x")



#Close the Toolkit.exe
time.sleep( 5 )
shell.SendKeys("%x")
print "Master Files Have Loaded Successfully"
