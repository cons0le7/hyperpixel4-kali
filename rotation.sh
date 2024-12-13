
#Uncomment the 2 lines below your chosen layout.


#LEFT (Landscape - HDMI & power port on bottom)

#DISPLAY=:0.0 xrandr --output DSI-1 --rotate left
#DISPLAY=:0.0 xinput set-prop "pointer:Goodix Capacitive TouchScreen" "libinput Calibration Matrix" 0 -1 1 1 0 0 0 0 1


#RIGHT (Landscape - HDMI & power port on top)

#DISPLAY=:0.0 xrandr --output DSI-1 --rotate right
#DISPLAY=:0.0 xinput set-prop "pointer:Goodix Capacitive TouchScreen" "libinput Calibration Matrix" 0 1 0 -1 0 1 0 0 1


#NORMAL (Portriat - HDMI & power port to the right)

#DISPLAY=:0.0 xrandr --output DSI-1 --rotate normal
#DISPLAY=:0.0 xinput set-prop "pointer:Goodix Capacitive TouchScreen" "libinput Calibration Matrix" 1 0 0 0 1 0 0 0 1


#INVERTED (Portriat - HDMI & power port to the left)

#DISPLAY=:0.0 xrandr --output DSI-1 --rotate inverted
#DISPLAY=:0.0 xinput set-prop "pointer:Goodix Capacitive TouchScreen" "libinput Calibration Matrix" -1 0 1 0 -1 1 0 0 1


