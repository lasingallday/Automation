#Loads C update files by automating UI

import win32com.client
import time
import SendKeys
import os

path = "L:/C_403/toolkit"
os.chdir( path )
shell = win32com.client.Dispatch("WScript.Shell") 

#Open the Toolkit.exe
os.startfile('L:/C_403/toolkit/toolkit.exe')

#Load the Product Update File
time.sleep( 5 )
shell.SendKeys("%t")
time.sleep( 1 )
shell.SendKeys("u")
time.sleep( 1 )
shell.SendKeys("p")
time.sleep( 1 )
shell.SendKeys("%r")
time.sleep( 1 )
shell.SendKeys("{ENTER}")
time.sleep( 1 )
shell.SendKeys("{ENTER}")
time.sleep( 1 )
shell.SendKeys("%x")

#Close the Toolkit.exe
time.sleep( 5 )
shell.SendKeys("%x")
print "Update Files Have Loaded Successfully"
