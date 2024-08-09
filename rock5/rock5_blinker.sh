#Sets RK3588 GPIOS 8 & 10 to a blinking state to let user know that autospeed.py is running.
#Setting gpio to LOW:
gpioset gpiochip0 14=0
gpioset gpiochip0 13=0
#Blinking loop:
#!/bin/bash

# Start the Python script in the background
python3 autospeed.py &

# Get the PID (Process ID) of the Python script
PYTHON_PID=$!

# Loop autospeed.py finishes
while kill -0 $PYTHON_PID 2>/dev/null; do
  gpioset gpiochip0 14=0
  gpioset gpiochip0 13=1
  sleep 0.5
  gpioset gpiochip0 13=0
  gpioset gpiochip0 14=1
  sleep 0.5
done
gpioset gpiochip0 14=0
gpioset gpiochip0 13=0
