# - NORMAL (Portriat - HDMI & power port to the right)

DISPLAY=:0.0 xrandr --output DSI-1 --rotate normal
DISPLAY=:0.0 xinput set-prop "pointer:Goodix Capacitive TouchScreen" "libinput Calibration Matrix" 1 0 0 0 1 0 0 0 1