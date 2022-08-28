@echo off
title Compiling DisFunc
echo Starting to compile DisFunc
pyinstaller DisFunc.py --uac-admin --onefile --noconsole
echo. 
echo Finished compiling DisFunc