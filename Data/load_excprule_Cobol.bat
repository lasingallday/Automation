@rem

REM    this sets up the directory where this batch file started 
REM  If you want another directory, need to define it.
set SourceDirectory=%cd%
@echo sourcedir %SourceDirectory%

REM This takes the first line of from file named version.txt and puts it in variable firstline

for /f tokens^=2^ delims^=^" %%p in (%SourceDirectory%\varfileCobol.py) do set CobolVersion^=%%p
@echo %CobolVersion%

L:
cd %CobolVersion%
start L:/%CobolVersion%/excload.exe
start L:/%CobolVersion%/excrpt.exe
PAUSE
