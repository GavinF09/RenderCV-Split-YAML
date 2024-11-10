echo Usage: setup.bat USERNAME [TEMPLATE=engineeringresumes]
@echo OFF
set PYTHON=.venv\Scripts\python.exe
if [%1]==[] (
  echo [X] Enter name as argument
  exit /b 1
)

if not [%3]==[] (
  echo [X] Only one argument allowed
  exit /b 2
)

echo [*] Name: %1
if [%2]==[] (
  echo [*] Initinalize with default template 'engineeringresumes'
  set TEMPLATE="engineeringresumes"
) else (
  set TEMPLATE=%2
)
echo [*] TEMPLATE: %TEMPLATE%

echo [+] Making Python Virtual Enviroment...
python -m venv .venv

echo [+] Installing libaries...
%PYTHON% -m pip install -r requirements.txt

echo [+] Initinalizing RenderCV...
%PYTHON% -m rendercv new %1 --theme %TEMPLATE%

:: pause