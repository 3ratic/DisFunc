@echo off
title Compiling DisFunc
echo Starting to compile DisFunc
pyinstaller source.py --uac-admin --onefile --noconsole
echo. 
echo Finished compiling DisFunc
