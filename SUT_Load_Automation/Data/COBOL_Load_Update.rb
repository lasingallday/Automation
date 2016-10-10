=begin

COBOL Load Update: Executes COBOL commands through command line to load update files

=end

require 'win32ole'

WIN32OLE.ole_initialize
system('start cmd.exe')
wsh = WIN32OLE.new('WScript.Shell')
sleep 1

wsh.SendKeys('L:')
wsh.SendKeys('{ENTER}')

wsh.SendKeys('cd Cobol 410')
wsh.SendKeys('{ENTER}')

wsh.SendKeys('tax021')
wsh.SendKeys('{ENTER}')
sleep 10

wsh.SendKeys('zip040')
wsh.SendKeys('{ENTER}')
sleep 10

wsh.SendKeys('tax007')
wsh.SendKeys('{ENTER}')
sleep 10

wsh.SendKeys('exit')
wsh.SendKeys('{ENTER}')