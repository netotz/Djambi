@echo off
echo Se instalara el sistema de gestion 'pip' y posteriormente el modulo 'colorama'.
echo Si ya tiene 'pip', que es lo mas probable, se instalara nuevamente. O puede no continuar y solo instalar 'colorama', escribiendo el comando:
echo.
echo pip install colorama
echo.
pause

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
del get-pip.py
pip install colorama

echo.
echo Instalacion finalizada
pause