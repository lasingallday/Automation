#Loads STEP control files by automating UI

import win32com.client
import time
import SendKeys
import os

path = "L:/C_407/toolkit"
os.chdir( path )
shell = win32com.client.Dispatch("WScript.Shell") 

#Open the Toolkit.exe
os.startfile('L:/C_407/toolkit/stepwin.exe')

#Load the Transaction File
time.sleep( 2 )
shell.SendKeys("%l")
time.sleep( 1 )
shell.SendKeys("{ENTER}")
time.sleep( 1 )
shell.SendKeys("{ENTER}")

#Load the Step Index Files
time.sleep( 2 )
shell.SendKeys("%l")
time.sleep( 1 )
shell.SendKeys("l")
time.sleep( 1 )
shell.SendKeys("{ENTER}")

#Load the Reason File
time.sleep( 2 )
shell.SendKeys("%l")
time.sleep( 1 )
shell.SendKeys("r")
time.sleep( 1 )
shell.SendKeys("{ENTER}")


#Close the Toolkit.exe
time.sleep( 2 )
shell.SendKeys("%l")
time.sleep( 1 )
shell.SendKeys("x")
print "Step Files Have Loaded Successfully"
