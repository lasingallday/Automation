import re
import os

def getMatchingName(filepath, matchString, situation):
	searchfile = open(filepath,'r')
	filetext = searchfile.read()
	searchfile.close()
	if situation == 'updateGenerateVersionFolder':
		situationString = '\w+' + 'T'
	if situation == 'updateFiles_PLSQL':
		situationString = 'ud'
	if situation == 'updateFiles_C':
		situationString = '\w+' + 'updt_'
	if situation == 'updateFiles_Cobol':
		situationString = '\w+' + 'upd'
	if situation == 'updateFiles_WorldTax':
		situationString = 'wtct'
	if situation == 'runningTaxtests':
		situationString = '_' + '\w+' + '-'
	if situation == 'LoadFiles':
		situationString = ''
	matchString = matchString + situationString + '\w+'
	s = re.findall(matchString,filetext)
	return s

def printResultsToFile(matchString, checkpath):
	os.chdir(checkpath)
	#os.chdir(u"T:/Departments/TaxContentQA/Test Artifacts & Results/SUT Content Update/2015 Folder/August 2015/Files/Update_Files")
	os.system("dir " + matchString + "* > " + "file.txt")
	os.system("set /p VAR=<" + "file.txt")


#printResultsToFile("taxtest", u"C:/Users/jeffrey.thomas/Desktop/Tests/SUT")
#getMatchingName(u"C:/Users/jeffrey.thomas/Desktop/Tests/SUT/taxtestfile.txt","taxtest")

#printResultsToFile("zip", u"T:/Departments/TaxContentQA/Test Artifacts & Results/SUT Content Update/2015 Folder/August 2015/Files/Update_Files")
