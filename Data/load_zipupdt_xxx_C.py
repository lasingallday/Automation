#Loads C update files by automating UI

import win32com.client
import time
import SendKeys
import os
from varfile import *

path = "L:/"+CVersion+"/toolkit"
os.chdir( path )
shell = win32com.client.Dispatch("WScript.Shell") 

#Open the Toolkit.exe
os.startfile(path+'/toolkit.exe')

#Load the Zip Update File
time.sleep( 5 )
shell.SendKeys("%t")
time.sleep( 1 )
shell.SendKeys("u")
time.sleep( 1 )
shell.SendKeys("z")
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
print "Update Files Have Loaded Successfully"

