@rem
@echo off
REM    this sets up the directory where this batch file started 
REM  If you want another directory, need to define it.
set SourceDirectory=%cd%
@echo sourcedir %SourceDirectory%

REM This takes the first line of from file named version.txt and puts it in variable firstline

for /f tokens^=2^ delims^=^" %%p in (%SourceDirectory%\varfileCobol.py) do set CobolVersion^=%%p
@echo %CobolVersion%

L:
cd %CobolVersion%
start tax021.exe
start zip010.exe
start zip080.exe
start tax006.exe
start excload.exe
start excrpt.exe
PAUSE