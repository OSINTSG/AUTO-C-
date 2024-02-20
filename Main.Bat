@echo off
echo Choose which script to run:
echo 1. WriteCode.py
echo 2. C++ Auto.py

choice /C 12 /N /M "Enter your choice:"

if errorlevel 2 (
    python "C++ Auto.py"
) else (
    python "WriteCode.py"
)
