import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# This removes ASCII characters, and writes them to a new, edited file.
with open('/Users/you/Downloads/sample.txt') as fp:
    edit_file = open('/Users/you/edited_sample.txt', "w")
    for line in iter(fp.readline, ''):
        decoded_line = str(line.decode('unicode_escape').encode('ascii', 'ignore'))
        edit_file.write(decoded_line)
    edit_file.close()
