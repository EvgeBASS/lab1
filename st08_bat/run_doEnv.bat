
::--------------------------------------
::Этот bat файл предназначен
::для создания виртуального окружения
::--------------------------------------

echo _My_ Create virtualenv on Python
pip install virtualenv
echo _My_ Create venv
python -m virtualenv venv
echo _My_ Switch to venv
CALL venv\Scripts\activate.bat
venv\Scripts\python.exe -m pip install --upgrade pip
echo _My_ Download lib
pip install requests
pip install flask
echo _My_ lib list
pip list
pause
