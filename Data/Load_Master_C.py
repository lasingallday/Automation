#Loads C master files by automating UI

import win32com.client
import time
import SendKeys
import os

path = "L:/C_407/toolkit"
os.chdir( path )
shell = win32com.client.Dispatch("WScript.Shell") 

#Open the Toolkit.exe
os.startfile('L:/C_407/toolkit/toolkit.exe')

#Load the Tax Master File
time.sleep( 5 )
shell.SendKeys("%t")
time.sleep( 1 )
shell.SendKeys("l")
time.sleep( 1 )
shell.SendKeys("t")
time.sleep( 1 )
shell.AppActivate('Sales/Use Tax System Toolkit') # Regains active focus on window
time.sleep( 1 )
shell.SendKeys("%r")
time.sleep( 1 )
shell.SendKeys("{ENTER}")
time.sleep( 1 )
shell.SendKeys("%x")

#Load the Zip Master File
time.sleep( 5 )
shell.SendKeys("%t")
time.sleep( 1 )
shell.SendKeys("l")
time.sleep( 1 )
shell.SendKeys("v")
time.sleep( 1 )
shell.SendKeys("z")
time.sleep( 1 )
shell.AppActivate('Sales/Use Tax System Toolkit') # Regains active focus on window
time.sleep( 1 )
shell.SendKeys("%r")
time.sleep( 1 )
shell.SendKeys("{ENTER}")
time.sleep( 1 )
shell.SendKeys("{ENTER}")
time.sleep( 1 )
shell.SendKeys("%x")

#Load the County Master File
time.sleep( 5 )
shell.SendKeys("%t")
time.sleep( 1 )
shell.SendKeys("l")
time.sleep( 1 )
shell.SendKeys("v")
time.sleep( 1 )
shell.SendKeys("c")
time.sleep( 1 )
shell.AppActivate('Sales/Use Tax System Toolkit') # Regains active focus on window
time.sleep( 1 )
shell.SendKeys("%r")
time.sleep( 1 )
shell.SendKeys("{ENTER}")
time.sleep( 1 )
shell.SendKeys("%x")

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

#Load the Product Master File
time.sleep( 5 )
shell.SendKeys("%t")
time.sleep( 1 )
shell.SendKeys("l")
time.sleep( 1 )
shell.SendKeys("p")
time.sleep( 1 )
shell.AppActivate('Sales/Use Tax System Toolkit') # Regains active focus on window
time.sleep( 1 )
shell.SendKeys("%r")
time.sleep( 1 )
shell.SendKeys("{ENTER}")
time.sleep( 1 )
shell.SendKeys("%x")


#Close the Toolkit.exe
time.sleep( 5 )
shell.SendKeys("%x")
print "Master Files Have Loaded Successfully"
