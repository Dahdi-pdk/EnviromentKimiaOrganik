@echo off
title Startup Belajar

:: Website
start msedge.exe https://chatgpt.com
timeout /t 2>nul
start msedge.exe https://notebooklm.google.com



timeout /t 2 >nul

:: Aplikasi
start code
start cmd
start explorer "D:\Project\Flask"
start explorer "D:\Kuliah"

exit