import xml.etree.ElementTree as ET
import sys
import re
from lxml import objectify, etree
from matchingNameFour import getMatchingName, printResultsToFile

#tree = ET.ElementTree(file='C:/Users/jeffrey.thomas/Results/FileLists.xml')
tree = ET.parse('C:/Users/jeffrey.thomas/Results/FileLists.xml')
with open('C:/Users/jeffrey.thomas/Results/FileLists.xml') as f:
	xml = f.read()
root_old = ET.Element("root")

#Initialize SubElements of the tree. objectify used because etree
#does not allow for writing of the tree.
versionNo = "649"
version = objectify.E.Version(versionNo)
etree.strip_attributes(version, '{http://codespeak.net/lxml/objectify/pytype}pytype')
etree.cleanup_namespaces(version)
#root_old.append(version)
systems = ET.SubElement(root_old, "Systems")
system = ET.SubElement(systems, "System")

count = 0
config_labels = ["Root","STEPFE_Content"]
filesDocLetters = []
COBOL_MainFiles = ['newmast','zipseq','prodseq','cntyseq','excprule']
C_MainFiles = ['newmast','zipseq','prodseq','cntyseq','excprule','feedata']
PLSQL_MainFiles = ['newmast','prodseq','excprule']
COBOL_incrementalFiles = []
C_incrementalFiles = ['taxupdt_652','zipupdt_349','produpdt_368']
PLSQL_incrementalFiles = []
updateResultsFolder = "T:/WIL/Departments/TaxContentQA/Test Artifacts & Results/SUT Content Update"
currentYearFolder = "/2016 Folder"
currentMonthYear_updateGenerate = "/March 2016"

printResultsToFile(matchString = "", checkpath = updateResultsFolder+currentYearFolder+currentMonthYear_updateGenerate+"/Regression/Files")
filesDocsLetters = getMatchingName(filepath = updateResultsFolder+currentYearFolder+currentMonthYear_updateGenerate+"/Regression/Files/file.txt", matchString = "", situation = "LoadFiles")
for filedocletter in filesDocsLetters:
	if (filedocletter in ['cntyseq','excprule']):
		COBOL_incrementalFiles.append(filedocletter)
#	if (filedocletter in ['cntyseq','excprule','feedata']):
#		C_incrementalFiles.append(filedocletter)
	if (filedocletter == 'excprule'):
		PLSQL_incrementalFiles.append(filedocletter)

incrementalFiles = getMatchingName(filepath = updateResultsFolder+currentYearFolder+currentMonthYear_updateGenerate+"/Regression/Files/file.txt", matchString = "", situation = "updateFiles_C")
#C_incrementalFiles.extend(incrementalFiles)
COBOL_incrementalFiles.extend(incrementalFiles)
regex = re.compile('zipupdt*')
PLSQL_incrementalFiles = [x for x in incrementalFiles if not regex.match(x)]

#*_Incremental_ControlFiles will be done in the LoadFiles loop
PLSQL_Full_ControlFiles = ["nexdesc","stepcnty","stepstre","taxholdy","txnexadm"]
PLSQL_Documents_text = ["Excprule.txt","DtChg649.txt","SmChg649.txt","SALESTAX.txt","stepcnty.txt","stepstre.txt","proddesc.txt","TAXHOLDY.txt","PRODUCT.txt","txnexadm.txt"]

#Looping to find specific Systems. cElementTree used because iterfind allows for specifying System Name.
#child: Type
#grandchild: 0-Configs, 1-Config, 2-Files
for elem in tree.iterfind('Systems'):
	for elem in tree.iterfind('Systems/System[@Name="C"]'):
		subel = objectify.E.Types()
		etree.cleanup_namespaces(subel)
		system.append(subel)
		child = ET.SubElement(subel,"Type")
		child.set("Name","Incremental")
		grandchild_0 = ET.SubElement(child,"Configs")
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","MainFiles")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for mainfile in C_incrementalFiles:
			file = objectify.E.File(mainfile)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","ControlFiles")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for controlfile in PLSQL_Full_ControlFiles:
			file = objectify.E.File(controlfile)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","Document")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for doc in PLSQL_Documents_text:
			file = objectify.E.File(doc)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
		child = ET.SubElement(subel,"Type")
		child.set("Name","Full")
		grandchild_0 = ET.SubElement(child,"Configs")
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","MainFiles")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for mainfile in C_MainFiles:
			file = objectify.E.File(mainfile)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
			
	for elem in tree.iterfind('Systems/System[@Name="PLSQL"]'):
		subel = objectify.E.Types()
		etree.cleanup_namespaces(subel)
		system.append(subel)
		child = ET.SubElement(subel,"Type")
		child.set("Name","Incremental")
		grandchild_0 = ET.SubElement(child,"Configs")
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","MainFiles")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for mainfile in PLSQL_incrementalFiles:
			file = objectify.E.File(mainfile)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","ControlFiles")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for controlfile in PLSQL_Full_ControlFiles:
			file = objectify.E.File(controlfile)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","Document")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for doc in PLSQL_Documents_text:
			file = objectify.E.File(doc)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
		child = ET.SubElement(subel,"Type")
		child.set("Name","Full")
		grandchild_0 = ET.SubElement(child,"Configs")
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","MainFiles")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for mainfile in PLSQL_MainFiles:
			file = objectify.E.File(mainfile)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
			
	for elem in tree.iterfind('Systems/System[@Name="COBOL"]'):
		subel = objectify.E.Types()
		etree.cleanup_namespaces(subel)
		system.append(subel)
		child = ET.SubElement(subel,"Type")
		child.set("Name","Incremental")
		grandchild_0 = ET.SubElement(child,"Configs")
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","MainFiles")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for mainfile in COBOL_incrementalFiles:
			file = objectify.E.File(mainfile)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","ControlFiles")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for controlfile in PLSQL_Full_ControlFiles:
			file = objectify.E.File(controlfile)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","Document")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for doc in PLSQL_Documents_text:
			file = objectify.E.File(doc)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
		child = ET.SubElement(subel,"Type")
		child.set("Name","Full")
		grandchild_0 = ET.SubElement(child,"Configs")
		grandchild_1 = ET.SubElement(grandchild_0,"Config")
		grandchild_1.set("Name","MainFiles")
		grandchild_2 = ET.SubElement(grandchild_1,"Files")
		for mainfile in COBOL_MainFiles:
			file = objectify.E.File(mainfile)
			etree.strip_attributes(file, '{http://codespeak.net/lxml/objectify/pytype}pytype')
			etree.cleanup_namespaces(file)
			grandchild_2.append(file)
	
tree.write("C:/Users/jeffrey.thomas/Desktop/New_FileLists.xml")
#x = etree.tostring(root_old, pretty_print=True)
#with open("C:/Users/jeffrey.thomas/Results/New_FileLists.xml", "w") as g:
	#g.write(x)
