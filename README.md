# HyperPixel 4.0 Drivers for Kali

HyperPixel 4.0 is an 800x480 or 720x720 pixel DPI display for Raspberry Pi, with optional capacitive touchscreen. 

*This fork has been optimized for compatibility with Kali OS. I got this working with 64 bit Kali for Raspberry Pi 4b. I am unsure if this will work for any other model or OS version. Any feedback will be greatly appreciated* 

## Installing 

Clone this repo: 
```
git clone https://github.com/cons0le7/hyperpixel4-kali
```
Paste into terminal: 
```
cd ~/hyperpixel4-kali 
chmod +x hyperpixel4-kali.sh
chmod +x rotation.sh
chmod +x keep_rotate.sh
./hyperpixel4-kali.sh
curl -sSL https://get.pimoroni.com/hyperpixel4-legacy | bash
```

When prompted, pick the combination of Pi and touchscreen that you're planning to use.

## Rotation (For Pi 4 and Pi 400)

Open config.txt in nano: 
```
sudo nano /boot/config.txt
```
uncomment `dtoverlay=vc4-fkms-v3d`

Set screen orientation by uncommenting your selection: 
```
cd ~/hyperpixel4-kali
sudo nano rotation.sh 
```

## You can make the rotation setting autostart at login by doing the following: 

### Navigate to startup settings: 
- tap the blue kali icon at the top right of desktop 
- Settings > Settings Manager > Session and Startup > Application Autostart > Add 
- Set a name and description.
- For command: 
```
/home/kali/hyperpixel4-kali/rotation.sh 
```
- Set trigger to ‘on login’ 

You can now do `sudo reboot` and login to make sure changes take affect. 
If done correctly the screen should be working and saved in the orientation you chose! 

# Issues: 
Feel free to open an issue in this repo or reach out to me on instagram `@con5ole` . 

