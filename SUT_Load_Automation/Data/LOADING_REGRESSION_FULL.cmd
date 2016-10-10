@echo off

cd ..\..\

REM set pythonloc=%cd%C:\Python27
REM set pyscriptsloc=%cd%C:\Python27\Scripts
REM set testloc=%cd%C:\Users\jeffrey.thomas\Results

cd Results

REM setlocal
REM set PATH=%PATH%;%pythonloc%;%pyscriptsloc%;%testloc%

START /WAIT CMD.exe /C pybot -t "Copy Regression B Files to Systems" SUT_Automation_Tests-Combined.txt

START /WAIT CMD.exe /C pybot -t "Master Control Load PLSQL" SUT_Automation_Tests-Combined.txt

START /WAIT CMD.exe /C pybot -t "Master Control Load C" SUT_Automation_Tests-Combined.txt

START /WAIT CMD.exe /C pybot -t "Master Control Load Cobol" SUT_Automation_Tests-Combined.txt

REM endlocal

exit /b 0