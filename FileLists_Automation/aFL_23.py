import xml.etree.ElementTree as ET
import sys
import re
import os
from lxml import objectify, etree
from matchingNameFour import getMatchingName, printResultsToFile
from varfile_FileLists import currentNoMonth, currentYear, updateResultsFolder, templateFolder, currentYearFolder, currentMonthYear_updateGenerate, supplementalNo

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem

tree = ET.parse('C:/Users/jeffrey.thomas/Desktop/FileLists.xml')

C_incrementalFiles = []
PLSQL_incrementalFiles = []
Cobol_incrementalFiles = []
RPG_incrementalFiles = []
Verazip_incrementalRoot = []
WorldTax_incrementalFiles = []
TMD_incrementalRoot = []
TMD2_incrementalRoot = []
TaxManager_incrementalRoot = []
Veratax_incrementalRoot = []
C_incrementalControlFiles = []
PLSQL_incrementalControlFiles = []
Cobol_incrementalControlFiles = []
RPG_incrementalControlFiles = []
WorldTax_incrementalControlFiles = []
C_incrementalDocuments = []
PLSQL_incrementalDocuments = []
Cobol_incrementalDocuments = []
RPG_incrementalDocuments = []
Cobol_incrementalCopyBooks = []
C_fullMainFiles = ['newmast','zipseq','prodseq','cntyseq','excprule','feedata']
PLSQL_fullMainFiles = ['newmast','prodseq','excprule']
Cobol_fullMainFiles = ['newmast','zipseq','prodseq','cntyseq','excprule']
C_fullControlFiles = ["canprovs","feedescs","feeexten","nexdesc","proddesc","prodext","stepreas","stepstcd","stepstcn","stepstrc","stepstre","taxbkt","taxbyitm","taxcuspd","taxdivpd","taxdlvr","taxdscpd","taxexc34","taxexczp","taxexmax","taxfees","taxfrtpd","taxholdy","taxholdy2","taxjurcd","taxjurpd","taxprizp","taxrfnds","taxrnd","taxrntpd","taxsrcpd","taxstapd","taxstuez","taxvalzp","texasexc","txbackex","txlocadm","txnexadm","txnobkst","txrndexc","txspdpd","txupdtno","zipstapd","zipvalzp","zpexs34","zpexseq","zpupdtno"]
PLSQL_fullControlFiles = ["nexdesc","PILoad.dat","proddesc","stepcnty.dat","stepreas","stepstcd","stepstcn","stepstrc","stepstre","taxbyitm","taxcuspd","taxdivpd","taxdscpd","taxexczp","taxfrtpd","taxholdy","taxholdy2","taxjurcd","taxjurpd","taxmxtax.dat","taxprizp","taxrntpd","taxsrcpd","taxstapd","taxvalzp","texasexc","txcanada.dat","txlocadm","txnexadm","txspdpd"]
Cobol_fullControlFiles = ["caltrtpd","prdistpd","stepreas","stepstcd","stepstcn","stepstrc","stepstre","taxbkt","taxbyitm","taxcuspd","taxexczp","taxfrtpd","taxholdy","taxholdy2","taxjurpd","taxjurpr","taxmappd","taxprizp","taxrnd","taxrntpd","taxsrcpd","taxstapd","texasexc","txrndexc","txspdpd","zipstapd","zpexseq"]
RPG_fullControlFiles = ["caltrtpd","gacntypd","prdistpd","stepstcd","taxfrcpd","taxfrtpd","taxholpd","taxholpd2","taxjurpd","taxmappd","taxrntpd","taxsrcpd.rpg","taxstapd.rpg","taxzippd","texasexc","txspdpd","zipstapd","zpexseq"]
Verazip_fullControlFiles = ["zpupdtno","zpexs34","zpexseq"]
WorldTax_fullControlFiles = ["wtcccf","wtcode","wtcompl","wtcomps","wtcurc","wtdltr","wtemplrn","wtiomsg","wtjury","wtmonth","wtmotr","wtnotc","wtrpvr","wtupdtno"]
C_fullDocuments = ["CANPROVS","Excprule","Feedata","feedescs","feeexten","proddesc","prodext","PRODUCT","SALESTAX","stepreas","stepstcd","stepstcn","stepstrc","stepstre","taxbkt","taxbyitm","TAXCUSPD","taxdscpd","taxexc34","taxexczp","TAXEXMAX","taxfrtpd","TAXHOLDY","TAXJURCD","TAXJURPD","Taxrfnds","taxrnd","TAXRNTPD","taxsrcpd","TAXSTAPD","taxstuez","taxvalzp","TEXASEXC","TXLOCADM","txnexadm","txrndexc","txspdpd","VERAZIP"]
PLSQL_fullDocuments = ["Excprule","proddesc","PRODUCT","SALESTAX","stepcnty","stepreas","stepstcd","stepstcn","stepstrc","stepstre","proddesc","taxbyitm","TAXCUSPD","taxdscpd","taxexczp","taxfrtpd","TAXHOLDY","TAXJURCD","TAXJURPD","taxmxtax","TAXRNTPD","taxsrcpd","TAXSTAPD","taxvalzp","TEXASEXC","TXLOCADM","txnexadm","txspdpd"]
Cobol_fullDocuments = ["caltrtpd","Excprule","prdistpd","PRODUCT","SALESTAX","proddescref","stepreas","stepstcd","stepstcn","stepstrc","stepstre","taxbkt","taxbyitm","TAXCUSPD","taxexczp","taxfrtpd","TAXHOLDY","TAXJURPD","TAXMAPPD","taxrnd","TAXRNTPD","taxsrcpd","TAXSTAPD","TEXASEXC","txrndexc","txspdpd","VERAZIP"]
RPG_fullDocuments = ["caltrtpd","gacntypd","prdistpd","PRODUCT","SALESTAX","stepstcd","TAXHOLPD","TAXJURPR","TAXMAPPD","TAXRNTPD","taxsrcpd","TAXSTAPD","taxzippd","TEXASEXC","txspdpd","VERAZIP"]
Verazip_fullDocuments = ["TAXJURPD","TAXMAPPD","VERAZIP"]

currentMonthYear_updateGenerate = "/"+currentMonthYear_updateGenerate
currentYearFolder = "/"+currentYearFolder

#get Control Files, which requires printing file lists for all three systems
printResultsToFile(matchString = "", checkpath = templateFolder+"/Files/Update/Control/C")
C_CFs = getMatchingName(filepath = templateFolder+"/Files/Update/Control/C/file.txt", matchString = "", situation = "LoadFiles")
printResultsToFile(matchString = "", checkpath = templateFolder+"/Files/Update/Control/PLSQL")
PLSQL_CFs = getMatchingName(filepath = templateFolder+"/Files/Update/Control/PLSQL/file.txt", matchString = "", situation = "LoadFiles")
printResultsToFile(matchString = "", checkpath = templateFolder+"/Files/Update/Control/Cobol")
Cobol_CFs = getMatchingName(filepath = templateFolder+"/Files/Update/Control/Cobol/file.txt", matchString = "", situation = "LoadFiles")
printResultsToFile(matchString = "", checkpath = templateFolder+"/Regression/Files")
RPG_Verazip_WorldTax_CFs = getMatchingName(filepath = templateFolder+"/Regression/Files/file.txt", matchString = "", situation = "LoadFiles")
for c_cf in C_CFs:
	if (c_cf in C_fullControlFiles):
		C_incrementalControlFiles.append(c_cf)
for plsql_cf in PLSQL_CFs:
	if (plsql_cf in PLSQL_fullControlFiles):
		PLSQL_incrementalControlFiles.append(plsql_cf)
for cobol_cf in Cobol_CFs:
	if (cobol_cf in Cobol_fullControlFiles):
		Cobol_incrementalControlFiles.append(cobol_cf)
for rpg_verazip_worldtax_cf in RPG_Verazip_WorldTax_CFs:
	if (rpg_verazip_worldtax_cf in RPG_fullControlFiles):
		RPG_incrementalControlFiles.append(rpg_verazip_worldtax_cf)
	if (rpg_verazip_worldtax_cf in Verazip_fullControlFiles):
		Verazip_incrementalRoot.append(rpg_verazip_worldtax_cf)
	if (rpg_verazip_worldtax_cf in WorldTax_fullControlFiles):
		WorldTax_incrementalControlFiles.append(rpg_verazip_worldtax_cf)

#get Documents for Control Files and Main Files
printResultsToFile(matchString = "", checkpath = templateFolder+"/Regression/Letters")
Docs = getMatchingName(filepath = templateFolder+"/Regression/Letters/file.txt", matchString = "", situation = "LoadFiles")
Docs_noInts = [x for x in Docs if not (x.isdigit() or x=='AM' or x=='PM')]
Docs_noInts_Compare = [item+'doc' for item in Docs_noInts]
C_Docs_Main_mixedCapitals = ['excprule','feedata']
PLSQL_Docs_Main_mixedCapitals = ['excprule']
for doc in Docs:
	if (doc.lower() in C_fullDocuments):
		C_incrementalDocuments.append(doc.lower() +".txt")
	if (doc.upper() in C_fullDocuments):
		C_incrementalDocuments.append(doc.upper() +".txt")
	#The next conditional has filenames where Main File and its Doc do not simply differ by capitalization.
	if (doc.lower() in C_Docs_Main_mixedCapitals):
		C_incrementalDocuments.append(doc+".txt")
	if (doc.lower() in PLSQL_fullDocuments):
		PLSQL_incrementalDocuments.append(doc.lower() +".txt")
	if (doc.upper() in PLSQL_fullDocuments):
		PLSQL_incrementalDocuments.append(doc.upper() +".txt")
	#The next conditional has filenames where Main File and its Doc do not simply differ by capitalization.
	if (doc.lower() in PLSQL_Docs_Main_mixedCapitals):
		PLSQL_incrementalDocuments.append(doc+".txt")
	if (doc.lower() in Cobol_fullDocuments):
		Cobol_incrementalDocuments.append(doc.lower() +".txt")
	if (doc.upper() in Cobol_fullDocuments):
		Cobol_incrementalDocuments.append(doc.upper() +".txt")
	#The next conditional has filenames where Main File and its Doc do not simply differ by capitalization.
	if (doc.lower() in PLSQL_Docs_Main_mixedCapitals):
		Cobol_incrementalDocuments.append(doc+".txt")
	if (doc.lower() in RPG_fullDocuments):
		RPG_incrementalDocuments.append(doc.lower() +".txt")
	if (doc.upper() in RPG_fullDocuments):
		RPG_incrementalDocuments.append(doc.upper() +".txt")
	if (doc.lower() in Verazip_fullDocuments):
		Verazip_incrementalRoot.append(doc.lower() +".txt")
	if (doc.upper() in Verazip_fullDocuments):
		Verazip_incrementalRoot.append(doc.upper() +".txt")
	if (doc == 'taxrfnds'):
		C_incrementalDocuments.append("Taxrfnds.txt")
	if (doc == 'zpexseq'):
		C_incrementalDocuments.append("VERAZIP.txt")
		Cobol_incrementalDocuments.append("VERAZIP.txt")
		RPG_incrementalDocuments.append("VERAZIP.txt")
		Verazip_incrementalRoot.append("VERAZIP.txt")

#Create the updateFiles list for adding Update Files	
updateFiles = getMatchingName(filepath = templateFolder+"/Regression/Files/file.txt", matchString = "", situation = "updateFiles_C")

#get Update Files, and add them to the Incremental Files
C_incrementalFiles.extend(updateFiles)
Cobol_incrementalFiles.extend(updateFiles)
RPG_incrementalFiles.extend(updateFiles)
regex = re.compile('zipupdt*')
PLSQL_incrementalFiles = [x for x in updateFiles if not regex.match(x)]

#get Update Files and add them--World Tax only
updateFiles_WT = getMatchingName(filepath = templateFolder+"/Regression/Files/file.txt", matchString = "", situation = "updateFiles_WorldTax")
WorldTax_incrementalFiles.extend(updateFiles_WT)

#get Main Files
printResultsToFile(matchString = "", checkpath = templateFolder+"/Regression/Files")
Files = getMatchingName(filepath = templateFolder+"/Regression/Files/file.txt", matchString = "", situation = "LoadFiles")
Files_noInts = [x for x in Files if not (x.isdigit() or x=='AM' or x=='PM')]
for file in Files_noInts:
	if (file in ['cntyseq','excprule','feedata']):
		C_incrementalFiles.append(file)
	if (file == 'excprule'):
		PLSQL_incrementalFiles.append(file)
	if (file in ['cntyseq','excprule']):
		Cobol_incrementalFiles.append(file)
	if (file == 'cntyseq'):
		RPG_incrementalFiles.append(file)
		Verazip_incrementalRoot.append(file)
	if (file == 'taxholdy'):
		Cobol_incrementalCopyBooks.append('TAXHOLTB')
		Cobol_incrementalCopyBooks.append('taxholtb2')
		
		#These files are troublesome because they are made on the PD ContentQA end, and they are not created by SCMS.
		#Note that filename+'doc' is not the name of the actual Document. It's just a shorthand for this Trouble Names section of code.
		trouble_names = set(['taxholdy','taxholdy2','taxholpd','taxholpd2','TAXHOLDYdoc','TAXHOLPDdoc'])
		FD_noInts = set(Files_noInts+Docs_noInts_Compare)
		intersection_taxholdy = FD_noInts.intersection(trouble_names)
		#Next line used for debugging
		#print(intersection_taxholdy)
		if (intersection_taxholdy != trouble_names):
			print("Intersection Taxholdy is missing related file(s)!")

#Add Docs with changing names. Then, check which Docs and Files were missed, based on existing files.
#Existing files are the file used in the current update, which we know by a 'Y' indicator on the month's Regression Report (in the SUT Zip Package Approval Tab).
taxupdate_no = ''
zipupdate_no = ''
for updatefile in updateFiles:
	if (updatefile[:7] == 'taxupdt'):
		taxupdate_no = updatefile[8:]
		C_incrementalDocuments.append("DtChg"+taxupdate_no+".txt")
		C_incrementalDocuments.append("SmChg"+taxupdate_no+".txt")
		PLSQL_incrementalDocuments.append("DtChg"+taxupdate_no+".txt")
		PLSQL_incrementalDocuments.append("SmChg"+taxupdate_no+".txt")
		Cobol_incrementalDocuments.append("DtChg"+taxupdate_no+".txt")
		Cobol_incrementalDocuments.append("SmChg"+taxupdate_no+".txt")
		RPG_incrementalDocuments.append("DtChg"+taxupdate_no+".txt")
		RPG_incrementalDocuments.append("SmChg"+taxupdate_no+".txt")
		TMD_incrementalRoot.append("DtChg"+taxupdate_no+".txt")
		TMD_incrementalRoot.append("SmChg"+taxupdate_no+".txt")
		TMD2_incrementalRoot.append("SmChg"+taxupdate_no+".txt")
		TaxManager_incrementalRoot.append("DtChg"+taxupdate_no+".txt")
		TaxManager_incrementalRoot.append("SmChg"+taxupdate_no+".txt")
		TaxManager_incrementalRoot.append("install.exe")
		TaxManager_incrementalRoot.append("TMD.txt")
		Veratax_incrementalRoot.append("DtChg"+taxupdate_no+".txt")
		Veratax_incrementalRoot.append("SmChg"+taxupdate_no+".txt")
		trouble_names = set(['TAXHOLTB','taxholtb2'])
		Files_noInts = set(Files_noInts)
		intersection_taxholtb = Files_noInts.intersection(trouble_names)
		if (intersection_taxholtb != trouble_names):
			print("Intersection Taxholtb is missing related file(s)!")
	if (updatefile[:7] == 'zipupdt'):
		zipupdate_no = updatefile[8:]
		Verazip_incrementalRoot.append(updatefile)
		print('zipupdt_'+zipupdate_no)
		trouble_names = set(['zipupdt_'+zipupdate_no,'VERAZIP.txt','zpupdtno'])
		intersection_zipupdt = FD_noInts.intersection(trouble_names)
		#if (intersection_zipupdt != trouble_names):
		#	print("Intersection Zipupdt is missing related file(s)!")


trouble_names = set(['proddesc','proddescrefdoc','proddescdoc'])
intersection_proddesc = FD_noInts.intersection(trouble_names)
#Next line used for debugging
#print(intersection_proddesc)
if (intersection_proddesc != trouble_names):
	print("If Proddesc is present, it is missing related file(s)!")
		
trouble_names = set(['cntyseq','stepcnty','tmdcnty','VERAZIPdoc','stepcntydoc'])
intersection_cntyseq = FD_noInts.intersection(trouble_names)
#Next line used for debugging
#print(intersection_cntyseq)
if (intersection_cntyseq != trouble_names):
	print("If Cntyseq present, it is missing related file(s)!\n")

#Current bug: cannot add TxManagerInstaller to trouble_names, for taxupdt, because it's a folder.
#Add code section like this for zipupdt
trouble_names = set(['taxupdt_'+taxupdate_no,'VERATAX','VTAXdoc','verataxPLUS','txupdtno','TMDFL','TAXMGRdoc'])
intersection_taxupdt = FD_noInts.intersection(trouble_names)
#Next line used for debugging
#print(intersection_taxupdt)
#print(trouble_names)
if (intersection_taxupdt != trouble_names):
	print("If Taxupdt is present, it is missing related file(s)!")


root = tree.getroot()

#Change all File's (File.text) to testinghere
#for elem in root.iter("File"):
#	elem.text = "testinghere"
#with open("C:/Users/jeffrey.thomas/Desktop/NF.xml", "w") as f:
#	tree.write(f)

#Change all Files for C System to newstuffhere
#for elem in root.findall("Systems/System[@Name='C']"):
#	for se in elem.iter("File"):
#		se.text = "newstuffhere"

#Insert Monthly Content Update's Metadata--Supplemental, Month, Year, Version
for supplemental in root.iter('Supplemental'):
	new_supplemental = int(supplementalNo)
	supplemental.text = '0'+str(new_supplemental)
for month in root.iter('Month'):
	#new_month = int(currentNoMonth)
	month.text = currentNoMonth
for year in root.iter('Year'):
	year.text = currentYear
for version in root.iter('Version'):
	version.text = taxupdate_no

#Sort the lists
C_incrementalFiles = sorted(C_incrementalFiles, key=lambda s: s.lower())
C_incrementalControlFiles = sorted(C_incrementalControlFiles, key=lambda s: s.lower())
C_incrementalDocuments = sorted(C_incrementalDocuments, key=lambda s: s.lower())
PLSQL_incrementalFiles = sorted(PLSQL_incrementalFiles, key=lambda s: s.lower())
PLSQL_incrementalControlFiles = sorted(PLSQL_incrementalControlFiles, key=lambda s: s.lower())
PLSQL_incrementalDocuments = sorted(PLSQL_incrementalDocuments, key=lambda s: s.lower())
Cobol_incrementalFiles = sorted(Cobol_incrementalFiles, key=lambda s: s.lower())
Cobol_incrementalControlFiles = sorted(Cobol_incrementalControlFiles, key=lambda s: s.lower())
Cobol_incrementalDocuments = sorted(Cobol_incrementalDocuments, key=lambda s: s.lower())
RPG_incrementalFiles = sorted(RPG_incrementalFiles, key=lambda s: s.lower())
RPG_incrementalControlFiles = sorted(RPG_incrementalControlFiles, key=lambda s: s.lower())
RPG_incrementalDocuments = sorted(RPG_incrementalDocuments, key=lambda s: s.lower())
Verazip_incrementalRoot = sorted(Verazip_incrementalRoot, key=lambda s: s.lower())
WorldTax_incrementalFiles = sorted(WorldTax_incrementalFiles, key=lambda s: s.lower())
WorldTax_incrementalControlFiles = sorted(WorldTax_incrementalControlFiles, key=lambda s: s.lower())
TMD_incrementalRoot = sorted(TMD_incrementalRoot, key=lambda s: s.lower())
TMD2_incrementalRoot = sorted(TMD2_incrementalRoot, key=lambda s: s.lower())
TaxManager_incrementalRoot = sorted(TaxManager_incrementalRoot, key=lambda s: s.lower())
Veratax_incrementalRoot = sorted(Veratax_incrementalRoot, key=lambda s: s.lower())

#Insert all files and documents
for elem in root.findall("Systems/System[@Name='C']/Types/Type[@Name='Incremental']/Configs/Config[@Name='MainFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(C_incrementalFiles)):
			File = ET.SubElement(se, "File")
			File.text = C_incrementalFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='C']/Types/Type[@Name='Incremental']/Configs/Config[@Name='ControlFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(C_incrementalControlFiles)):
			File = ET.SubElement(se, "File")
			File.text = C_incrementalControlFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='C']/Types/Type[@Name='Incremental']/Configs/Config[@Name='Documents']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(C_incrementalDocuments)):
			File = ET.SubElement(se, "File")
			File.text = C_incrementalDocuments[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='PLSQL']/Types/Type[@Name='Incremental']/Configs/Config[@Name='MainFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(PLSQL_incrementalFiles)):
			File = ET.SubElement(se, "File")
			File.text = PLSQL_incrementalFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='PLSQL']/Types/Type[@Name='Incremental']/Configs/Config[@Name='ControlFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(PLSQL_incrementalControlFiles)):
			File = ET.SubElement(se, "File")
			File.text = PLSQL_incrementalControlFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='PLSQL']/Types/Type[@Name='Incremental']/Configs/Config[@Name='Documents']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(PLSQL_incrementalDocuments)):
			File = ET.SubElement(se, "File")
			File.text = PLSQL_incrementalDocuments[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='COBOL']/Types/Type[@Name='Incremental']/Configs/Config[@Name='MainFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(Cobol_incrementalFiles)):
			File = ET.SubElement(se, "File")
			File.text = Cobol_incrementalFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='COBOL']/Types/Type[@Name='Incremental']/Configs/Config[@Name='ControlFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(Cobol_incrementalControlFiles)):
			File = ET.SubElement(se, "File")
			File.text = Cobol_incrementalControlFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='COBOL']/Types/Type[@Name='Incremental']/Configs/Config[@Name='CICS-CopyBooks']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(Cobol_incrementalCopyBooks)):
			File = ET.SubElement(se, "File")
			File.text = Cobol_incrementalCopyBooks[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='COBOL']/Types/Type[@Name='Incremental']/Configs/Config[@Name='Documents']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(Cobol_incrementalDocuments)):
			File = ET.SubElement(se, "File")
			File.text = Cobol_incrementalDocuments[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='RPG']/Types/Type[@Name='Incremental']/Configs/Config[@Name='MainFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(RPG_incrementalFiles)):
			File = ET.SubElement(se, "File")
			File.text = RPG_incrementalFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='RPG']/Types/Type[@Name='Incremental']/Configs/Config[@Name='ControlFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(RPG_incrementalControlFiles)):
			File = ET.SubElement(se, "File")
			File.text = RPG_incrementalControlFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='RPG']/Types/Type[@Name='Incremental']/Configs/Config[@Name='Documents']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(RPG_incrementalDocuments)):
			File = ET.SubElement(se, "File")
			File.text = RPG_incrementalDocuments[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='Verazip']/Types/Type[@Name='Incremental']/Configs/Config[@Name='Root']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(Verazip_incrementalRoot)):
			File = ET.SubElement(se, "File")
			File.text = Verazip_incrementalRoot[filecount]#Add the new file

#If sections are empty, file/files divisions in the emption section will not be right
for elem in root.findall("Systems/System[@Name='WorldTax']/Types/Type[@Name='Incremental']/Configs/Config[@Name='MainFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(WorldTax_incrementalFiles)):
			File = ET.SubElement(se, "File")
			File.text = WorldTax_incrementalFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='WorldTax']/Types/Type[@Name='Incremental']/Configs/Config[@Name='ControlFiles']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(WorldTax_incrementalControlFiles)):
			File = ET.SubElement(se, "File")
			File.text = WorldTax_incrementalControlFiles[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='TMD']/Types/Type[@Name='Incremental']/Configs/Config[@Name='Root']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(TMD_incrementalRoot)):
			File = ET.SubElement(se, "File")
			File.text = TMD_incrementalRoot[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='TMD2']/Types/Type[@Name='Incremental']/Configs/Config[@Name='Root']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(TMD2_incrementalRoot)):
			File = ET.SubElement(se, "File")
			File.text = TMD2_incrementalRoot[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='TaxManager']/Types/Type[@Name='Full']/Configs/Config[@Name='Root']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(TaxManager_incrementalRoot)):
			File = ET.SubElement(se, "File")
			File.text = TaxManager_incrementalRoot[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='Veratax']/Types/Type[@Name='Full']/Configs/Config[@Name='Root']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(Veratax_incrementalRoot)):
			File = ET.SubElement(se, "File")
			File.text = Veratax_incrementalRoot[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='C']/Types/Type[@Name='Full']/Configs/Config[@Name='Documents']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(C_incrementalDocuments)):
			File = ET.SubElement(se, "File")
			File.text = C_incrementalDocuments[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='PLSQL']/Types/Type[@Name='Full']/Configs/Config[@Name='Documents']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(PLSQL_incrementalDocuments)):
			File = ET.SubElement(se, "File")
			File.text = PLSQL_incrementalDocuments[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='COBOL']/Types/Type[@Name='Full']/Configs/Config[@Name='Documents']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(Cobol_incrementalDocuments)):
			File = ET.SubElement(se, "File")
			File.text = Cobol_incrementalDocuments[filecount]#Add the new file

for elem in root.findall("Systems/System[@Name='RPG']/Types/Type[@Name='Full']/Configs/Config[@Name='Documents']"):
	for se in elem.iter("Files"):
		for filecount in range(0,len(RPG_incrementalDocuments)):
			File = ET.SubElement(se, "File")
			File.text = RPG_incrementalDocuments[filecount]#Add the new file

tree.write("C:/Users/jeffrey.thomas/Desktop/New_FileLists.xml")
tree_indented = ET.parse("C:/Users/jeffrey.thomas/Desktop/New_FileLists.xml")
root_indented = tree_indented.getroot()
indent(root_indented)
tree_indented.write("C:/Users/jeffrey.thomas/Desktop/New_FileLists_indented.xml")
