@echo off
echo 🧠 Setting up LanAI...
cd %~dp0

REM Cria o ambiente virtual
python -m venv venv

REM Ativa o ambiente
call venv\Scripts\activate.bat

REM Atualiza o pip e instala dependências
echo 🧪 Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

echo ✅ LanAI is ready!
echo.
python lanai.py
pause
