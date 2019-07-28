import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# This removes ASCII characters, and writes them to a new, edited file.
with open('/Users/jif/Repos/Automation/Files/sample.txt') as fp:
    edit_file = open('/Users/jif/Repos/Automation/Files/sample_v2.txt', "w")
    for line in fp:
        edit_file.write(line)
    edit_file.close()
