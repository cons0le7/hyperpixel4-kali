# HyperPixel 4.0 Drivers for Kali 2024.3

HyperPixel 4.0 is an 800x480 or 720x720 pixel DPI display for Raspberry Pi, with optional capacitive touchscreen. 

*This fork has been created to simplify setup of HyperPixel 4.0 screen with kali OS. I've got this working with 64 bit Kali ARM 2024.3 for Raspberry Pi 4b with rectangular screen (kali-linux-2024.3-raspberry-pi-arm64.img.xz) I am unsure if this will work for any other model or OS version. Any feedback / bug reports would be greatly appreciated.*  

I have got this working thanks to [Massi361](https://github.com/Massi361)'s solution posted here: 
https://github.com/pimoroni/hyperpixel/issues/52

![IMG_2890](https://github.com/user-attachments/assets/f9f9ada8-70e5-4361-8e42-eeb43693cb72)

## Before installation: 
After flashing Kali to your micro SD, it is recommended to backup your config file in `boot/config.txt`. In the case you end up with a blank screen or get stuck on the rainbow screen when rebooting after a failed driver install, you can try replacing the config file with the original and this may save you from having to flash the OS again. 

## Easy install:
Clone this repo: 
```
git clone https://github.com/cons0le7/hyperpixel4-kali
```
Paste into terminal: 
```
cd hyperpixel4-kali
python3 easy.py 
```
You will be presented with 4 options: 

### Install 
Initial setup of driver. Follow the prompts during install to ensure proper setup.
### Update Config 
Necessary for rotation to work. This adds `dtoverlay=vc4-fkms-v3d` in /boot/config.txt 
### Rotate Display 
This can be accessed any time for on the fly rotation. you can also use the `rotate.py` file as a stand-alone rotation tool. 
### Setup Persistence: 
This has been updated to automatically save X11 config settings based on your selection of display type and orientation. This will ensure your display orientation remains as selected even after rebooting. 
I left the legacy option with instructions for setting up manually in autostart if for some reason you prefer this route or have any issues with the auto-config not working. 

_________________________________________

*Nothing beyond this point is necessarry if you chose to use the easy install.*
_________________________________________


## Manual installation:  

Clone this repo: 
```
git clone https://github.com/cons0le7/hyperpixel4-kali
```
Paste into terminal: 
```
cd ~/hyperpixel4-kali 
chmod +x hyperpixel4-kali.sh
chmod +x rotation.sh
./hyperpixel4-kali.sh
curl -sSL https://get.pimoroni.com/hyperpixel4-legacy | bash
```

When prompted, pick the combination of Pi and screen that you're planning to use.

## Rotation (For Pi 4 and Pi 400)

Open config.txt in nano: 
```
sudo nano /boot/config.txt
```
uncomment `dtoverlay=vc4-fkms-v3d`

save and exit. 

Set screen orientation by uncommenting your selection in 'rotation.sh': 
```
cd ~/hyperpixel4-kali
sudo nano rotation.sh 
```

### To make rotation settings stay after reboot / power off: 
- tap the blue kali icon at the top left of desktop 
- Settings > Settings Manager > Session and Startup > Application Autostart > Add 
- Set a name and description.
- For command: 
```
/home/kali/hyperpixel4-kali/rotation.sh 
```
- Set trigger to ‘on login’ 

You can now do `sudo reboot` and login to make sure changes take affect. 
If done correctly the screen should be working and saved in the orientation you chose.


## On-the-fly rotation: 

The 'square-rotos' and 'rectangular-rotos' folders in this repo contain individual .sh files which can be made executable: 

- Rectangular:
```
chmod +x ~/hyperpixel4-kali/rectangular-rotos/*.sh
```

- Square:
```
chmod +x ~/hyperpixel4-kali/square-rotos/*.sh
```
After being made executable, you can double click any of them and execute in terminal for on-the-fly rotation. You can move these files anywhere or make desktop shortcuts if you'd like.

# Issues: 
Feel free to open an issue in this repo or reach out to me on instagram `@con5ole` . 

