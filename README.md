# Archivos para lanzar tests a movispeed
Libreria con archivos de prueba para lanzar tests de forma automática a movispeed desde una PCB (rock pi) 
para acelerar las pruebas en instalaciones FTTH Movistar.




# Instrucciones:
sudo apt-get update
sudo apt-get upgrade
sudo apt install python3
sudo apt install python3-pip
pip install playwright --break-system-packages
python3 -m playwright install
playwright install-deps

#para ssh:
passwd 
#En windows
ssh-keygen -R 192.168.1.62
