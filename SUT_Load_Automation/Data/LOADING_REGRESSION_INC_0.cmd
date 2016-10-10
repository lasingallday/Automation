@echo off

cd ..\..\

REM set pythonloc=%cd%C:\Python27
REM set pyscriptsloc=%cd%C:\Python27\Scripts
REM set testloc=%cd%C:\Users\jeffrey.thomas\Results

cd Results

REM setlocal
REM set PATH=%PATH%;%pythonloc%;%pyscriptsloc%;%testloc%

START /WAIT CMD.exe /C pybot -v testType:Regression -t "Copy Non Update Files to ContentQA" SUT_Automation_Tests-Combined.txt

START /WAIT CMD.exe /C pybot -t "Copy Regression A Files to Systems" SUT_Automation_Tests-Combined.txt

START /WAIT CMD.exe /C pybot -t "Add" SUT_Automation_Tests-Combined.txt

START /WAIT CMD.exe /C pybot -t "New Master Load" SUT_Automation_Tests-Combined.txt

REM endlocal

exit /b 0