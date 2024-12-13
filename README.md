# HyperPixel 4.0" Drivers

HyperPixel 4.0 is an 800x480 or 720x720 pixel DPI display for Raspberry Pi, with optional capacitive touchscreen. 
*This fork has been optimized for compatibility with Kali OS.* 

## Installing / Uninstalling 

clone this repo: 
```
git clone https://github.com/cons0le7/hyperpixel4-kali
```
Then: 
```
cd ~/hyperpixel4-kali 
chmod +x hyperpixel4-kali.sh
./hyperpixel4-kali.sh
```
Install driver: 
```
curl -sSL https://get.pimoroni.com/hyperpixel4-legacy | bash
```

When prompted, pick the combination of Pi and touchscreen that you're planning to use.

Note: A HyperPixel4 setup for Pi 3B+ or earlier will not readily work if you move it over to a Pi 4, you should run this installer again to update the drivers.

## Rotation

for Pi 4 and Pi 400
```
sudo nano /boot/config.txt
```
uncomment `dtoverlay=vc4-fkms-v3d`

### Rotation on the fly

You can use xrandr and xinput to rotate the display and touchscreen in turn.

For HyperPixel Square, substitute the device name with "pointer:generic ft5x06 (11)".

#### Left

```
DISPLAY=:0.0 xrandr --output DSI-1 --rotate left
DISPLAY=:0.0 xinput set-prop "pointer:Goodix Capacitive TouchScreen" "libinput Calibration Matrix" 0 -1 1 1 0 0 0 0 1
```

#### Right

```
DISPLAY=:0.0 xrandr --output DSI-1 --rotate right
DISPLAY=:0.0 xinput set-prop "pointer:Goodix Capacitive TouchScreen" "libinput Calibration Matrix" 0 1 0 -1 0 1 0 0 1
```

#### Normal

```
DISPLAY=:0.0 xrandr --output DSI-1 --rotate normal
DISPLAY=:0.0 xinput set-prop "pointer:Goodix Capacitive TouchScreen" "libinput Calibration Matrix" 1 0 0 0 1 0 0 0 1
```

#### Inverted

```
DISPLAY=:0.0 xrandr --output DSI-1 --rotate inverted
DISPLAY=:0.0 xinput set-prop "pointer:Goodix Capacitive TouchScreen" "libinput Calibration Matrix" -1 0 1 0 -1 1 0 0 1
```



