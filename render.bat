@echo OFF

set PYTHON=.venv\Scripts\python.exe

echo [+] Compiling YAML files from ./content
%PYTHON% ./combine_yaml.py
if not %errorlevel%==0 (
    echo [X] Something went wrong with combining the YAML files 
    exit /b 1
)

echo [+] Running RenderCV render command
%PYTHON% -m rendercv render rendercvResume.yaml
