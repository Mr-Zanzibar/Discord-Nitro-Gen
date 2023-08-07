@echo off
title Nitro Gen

:: This script will run the python script that will run the program
:: It will also check if python is installed and if it is in PATH
:: If it is not, it will tell you to install it and put it in PATH

where python
IF %ERRORLEVEL% NEQ 0 (
  cls
  echo You might need to install python first!
  echo https://www.python.org/downloads/
  echo.
  echo If you do already have it installed, you might have forgotten to put it in PATH
  echo Reinstall it and make sure to check the box that says "Add Python to PATH"
  echo.

  pause
  exit
)

python gen.py

pause
exit
