# - INVERTED (Portriat - HDMI & power port to the left)

DISPLAY=:0.0 xrandr --output DSI-1 --rotate inverted
DISPLAY=:0.0 xinput set-prop "pointer:generic ft5x06 (11)" "libinput Calibration Matrix" -1 0 1 0 -1 1 0 0 1

