# HyperPixel 4.0" Drivers

HyperPixel 4.0 is an 800x480 or 720x720 pixel DPI display for Raspberry Pi, with optional capacitive touchscreen. 
*This fork has been optimized for compatibility with Kali OS.* 

## Installing / Uninstalling (Legacy)

clone this repo: 
```
git clone https://github.com/cons0le7/hyperpixel4-kali/tree/master
```
Then: 
```
chmod +x hyperpixel4-kali.sh
./hyperpixel4-kali.sh
```
Install driver: 
```
curl -sSL https://get.pimoroni.com/hyperpixel4-legacy | bash
```

When prompted, pick the combination of Pi and touchscreen that you're planning to use.

Note: A HyperPixel4 setup for Pi 3B+ or earlier will not readily work if you move it over to a Pi 4, you should run this installer again to update the drivers.


### Manual Installation

Here's a list of active branches and which Pi/display combination they support:

* [pi3](https://github.com/pimoroni/hyperpixel4/tree/pi3) - Pi 3B+ and earlier, HyperPixel4 Rectangular
* [pi4](https://github.com/pimoroni/hyperpixel4/tree/pi4) - Pi 4 & Pi 400, HyperPixel4 Rectangular, use `hyperpixel4-rotate` to rotate once installed
* [square](https://github.com/pimoroni/hyperpixel4/tree/square) - Pi 3B+ and earlier, HyperPixel4 Square (for boards manufactured 2020 and earlier)
* [square-pi4](https://github.com/pimoroni/hyperpixel4/tree/square-pi4)  - Pi 4 & Pi 400, HyperPixel4 Square (for boards manufactured 2020 and earlier)
* [square-2021](https://github.com/pimoroni/hyperpixel4/tree/square-2021) - Pi 3B+ and earlier, HyperPixel4 Square (for boards manufactured 2021 and later)
* [square-pi4-2021](https://github.com/pimoroni/hyperpixel4/tree/square-pi4-2021)  - Pi 4 & Pi 400, HyperPixel4 Square (for boards manufactured 2021 and later)

To clone a specific branch to your Pi, run:

```
git clone https://github.com/pimoroni/hyperpixel4 -b <branch name>
```

Then `cd hyperpixel4` and run `sudo ./install.sh` to install it.

## Rotation

## Totally Manual Rotation

:warning: for Xorg-based operating systems running on Pi 4 and Pi 400
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


## Troubleshooting

Where possible we are collecting known FAQs under the `notice` label in our issue tracker.

[`Notice` Issue Tracker](https://github.com/pimoroni/hyperpixel4/issues?q=is%3Aissue+label%3Anotice+)

If your issue is not covered by one of these provided by our team and community 
then we ask you to provide some debugging information using the following oneliner:

```bash
curl -sSL https://raw.githubusercontent.com/pimoroni/hyperpixel4/master/hyperpixel4-debug.sh | bash
```

Then [file a bug report](https://github.com/pimoroni/hyperpixel4/issues/new/choose).


