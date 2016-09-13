#Loads C master files by automating UI

import win32com.client
import time
import SendKeys
import subprocess
from datetime import datetime

subprocess.call('move /y 2016-02-sut-cobol-regular-full\MainFiles\* "T:\WIL\Departments\TaxContentQA\Test Artifacts & Results\Special_Projects\SUT Automation\Template\Files\Prod\Main\Cobol"',shell=True)
subprocess.call('copy /y 2016-02-sut-c-regular-full\MainFiles\zipseq "T:\WIL\Departments\TaxContentQA\Test Artifacts & Results\Special_Projects\SUT Automation\Template\Files\Prod\Main\PLSQL"',shell=True)
subprocess.call('move /y 2016-02-sut-c-regular-full\MainFiles\* "T:\WIL\Departments\TaxContentQA\Test Artifacts & Results\Special_Projects\SUT Automation\Template\Files\Prod\Main\C"',shell=True)
subprocess.call('move /y 2016-02-sut-plsql-regular-full\MainFiles\* "T:\WIL\Departments\TaxContentQA\Test Artifacts & Results\Special_Projects\SUT Automation\Template\Files\Prod\Main\PLSQL"',shell=True)
