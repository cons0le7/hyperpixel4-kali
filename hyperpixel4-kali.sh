#!/bin/bash
sudo apt install python3-dev 
sudo apt install python3-rpi.gpio 
FILE="/usr/bin/hyperpixel4-init"
[ -f "$FILE" ] && sed -i '1s/python/python3/' "$FILE"