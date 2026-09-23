@echo off

cd /d "%~dp0\..\.."

call .venv\Scripts\activate.bat

robot --outputdir .\02_Script_Running_Options\reports .\02_Script_Running_Options\code\execution_demo.robot

pause