# - LEFT (Landscape - HDMI & power port on bottom)

DISPLAY=:0.0 xrandr --output DSI-1 --rotate left
DISPLAY=:0.0 xinput set-prop "pointer:generic ft5x06 (11)" "libinput Calibration Matrix" 0 -1 1 1 0 0 0 0 1