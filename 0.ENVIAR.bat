python --version

@REM se retornou erro, instala python
@REM Retorno 0 OK, retorno 1 NOK

@REM if errorlevel 1 (
@REM     echo NAO HA PYTHON INSTLALADO
@REM )
@REM
@REM if errorlevel 0 (
@REM     python cadastro.py
@REM )

echo Executar envio dos boletos
python cadastro.py

@REM Aguardara ultimo comando para fechar janela
pause
