#!/bin/bash

#crontab -l
# añadir ultimas lineas de https://github.com/Nenter/movispeed/blob/main/rock5/crontab
#
#@reboot /home/nenter/script_movispeed.sh
#* * * * * /home/nenter/script_movispeed.sh
#
#Activa entorno virtual
source "/home/nenter/venv/bin/activate"
#ejecuta python3 desde entorno virtual
python3 /home/nenter/Desktop/autospeed.py
