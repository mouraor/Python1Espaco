python --version

@REM se retornou erro, instala python
@REM Retorno 0 OK, retorno 1 NOK

if errorlevel 1 (
    echo NAO HA PYTHON INSTLALADO
)

if errorlevel 0 (
    python cadastro.py
)

pause
