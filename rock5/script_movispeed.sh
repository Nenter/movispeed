#!/bin/bash

#crontab -l
# añadir ultimas lineas de https://github.com/Nenter/movispeed/blob/main/rock5/crontab
#
#@reboot /home/nenter/script_movispeed.sh
#* * * * * /home/nenter/script_movispeed.sh
#
#gpiodlib gpioset gpiochipX GPIOPIN=1; 1:HIGH, 0:LOW

python3 autospeed.py
