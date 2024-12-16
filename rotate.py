import os 
import sys 

def rectangle_left(): 
    os.system("DISPLAY=:0.0 xrandr --output DSI-1 --rotate left")
    os.system("DISPLAY=:0.0 xinput set-prop \"pointer:Goodix Capacitive TouchScreen\" \"libinput Calibration Matrix\" 0 -1 1 1 0 0 0 0 1")
def rectangle_right(): 
    os.system("DISPLAY=:0.0 xrandr --output DSI-1 --rotate right")
    os.system("DISPLAY=:0.0 xinput set-prop \"pointer:Goodix Capacitive TouchScreen\" \"libinput Calibration Matrix\" 0 1 0 -1 0 1 0 0 1")
def rectangle_default(): 
    os.system("DISPLAY=:0.0 xrandr --output DSI-1 --rotate normal")
    os.system("DISPLAY=:0.0 xinput set-prop \"pointer:Goodix Capacitive TouchScreen\" \"libinput Calibration Matrix\" 1 0 0 0 1 0 0 0 1")
def rectangle_inverted(): 
    os.system("DISPLAY=:0.0 xrandr --output DSI-1 --rotate inverted")
    os.system("DISPLAY=:0.0 xinput set-prop \"pointer:Goodix Capacitive TouchScreen\" \"libinput Calibration Matrix\" -1 0 1 0 -1 1 0 0 1")
    
def square_left(): 
    os.system("DISPLAY=:0.0 xrandr --output DSI-1 --rotate left")
    os.system("DISPLAY=:0.0 xinput set-prop \"pointer:generic ft5x06 (11)\" \"libinput Calibration Matrix\" 0 -1 1 1 0 0 0 0 1")
def square_right(): 
    os.system("DISPLAY=:0.0 xrandr --output DSI-1 --rotate right")
    os.system("DISPLAY=:0.0 xinput set-prop \"pointer:generic ft5x06 (11)\" \"libinput Calibration Matrix\" 0 1 0 -1 0 1 0 0 1")
def square_default(): 
    os.system("DISPLAY=:0.0 xrandr --output DSI-1 --rotate normal")
    os.system("DISPLAY=:0.0 xinput set-prop \"pointer:generic ft5x06 (11)\" \"libinput Calibration Matrix\" 1 0 0 0 1 0 0 0 1")
def square_inverted(): 
    os.system("DISPLAY=:0.0 xrandr --output DSI-1 --rotate inverted")
    os.system("DISPLAY=:0.0 xinput set-prop \"pointer:generic ft5x06 (11)\" \"libinput Calibration Matrix\" -1 0 1 0 -1 1 0 0 1")
    
def rectangle(): 
    rotate_rectangle = int(input("""
    Rotate 
    [1] Left 
    [2] Right 
    [3] Default 
    [4] Inverted 
    [5] Exit
    """))
    if rotate_rectangle == 1:
        rectangle_left()
        rectangle()
    elif rotate_rectangle == 2:
        rectangle_right()
        rectangle()
    elif rotate_rectangle == 3: 
        rectangle_default()
        rectangle()
    elif rotate_rectangle == 4: 
        rectangle_inverted()
        rectangle()
    elif rotate_rectangle == 5:
        sys.exit()
    else: 
        print("Invalid input. Enter a number 1-5")
        rectangle()
    
def square(): 
    rotate_square = int(input("""
    Rotate 
    [1] Left 
    [2] Right 
    [3] Default 
    [4] Inverted 
    [5] Exit
    """))
    if rotate_square == 1:
        square_left()
        square()
    elif rotate_square == 2:
        square_right()
        square()
    elif rotate_square == 3: 
        square_default()
        square()
    elif rotate_square == 4: 
        square_inverted()
        square()
    elif rotate_square == 5:
        sys.exit()
    else: 
        print("Invalid input. Enter a number 1-5")
        square()
    
def menu(): 
    display = int(input("""
    Select your display type: 
    [1] Rectangular 
    [2] Square 
    [3] Exit 
    """))
    if display == 1:
        rectangle() 
    elif display == 2: 
        square() 
    elif display == 3: 
        sys.exit()
    else: 
        print("Invalid input. Enter a number 1-3.")
        menu()
menu()
        
    
