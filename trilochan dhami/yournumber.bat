@echo off
setlocal enabledelayedexpansion

rem Input variables
set /p rootDirectory=Enter the name of the root directory:
if "%rootDirectory%" == "" (
echo Error: Root directory name cannot be empty.
pause
exit /b
)

rem Create root directory
mkdir %rootDirectory%
cd %rootDirectory%

rem Loop to create subdirectories and files
:loop
set /p subDirectory=Enter the name of a subdirectory or type exit to finish:
if "%subDirectory%" == "exit" (
cd ..
echo Root directory structure created successfully!
pause
exit /b
)
mkdir %subDirectory%
cd %subDirectory%

set /p fileName=Enter the name of a file or type exit to go back to the previous directory:
if "%fileName%" == "exit" (
cd ..
goto loop
)
echo Test content > %fileName%.txt
goto loop