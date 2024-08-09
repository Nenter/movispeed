#!/bin/bash

file_path="test_file.txt"
read -r success download upload < "$file_path"
gpioset gpiochip0 14=0
gpioset gpiochip0 13=0
