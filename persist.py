import os

rectangle_left = """
Section "InputClass"
    Identifier "libinput HyperPixel4 Rectangular"
    MatchProduct "Goodix Capacitive TouchScreen"
    Option "CalibrationMatrix" "0 -1 1 1 0 0 0 0 1"
EndSection

Section "Monitor"
    Identifier "DSI-1"
    Option "Rotate" "left"
EndSection
"""

rectangle_right = """
Section "InputClass"
    Identifier "libinput HyperPixel4 Rectangular"
    MatchProduct "Goodix Capacitive TouchScreen"
    Option "CalibrationMatrix" "0 1 0 -1 0 1 0 0 1"
EndSection

Section "Monitor"
    Identifier "DSI-1"
    Option "Rotate" "right"
EndSection
"""

rectangle_default = """
Section "InputClass"
    Identifier "libinput HyperPixel4 Rectangular"
    MatchProduct "Goodix Capacitive TouchScreen"
    Option "CalibrationMatrix" "1 0 0 0 1 0 0 0 1"
EndSection

Section "Monitor"
    Identifier "DSI-1"
    Option "Rotate" "default"
EndSection
"""

rectangle_inverted = """
Section "InputClass"
    Identifier "libinput HyperPixel4 Rectangular"
    MatchProduct "Goodix Capacitive TouchScreen"
    Option "CalibrationMatrix" "-1 0 1 0 -1 1 0 0 1"
EndSection

Section "Monitor"
    Identifier "DSI-1"
    Option "Rotate" "inverted"
EndSection
"""

square_left = """
Section "InputClass"
    Identifier "libinput HyperPixel4 Square"
    MatchProduct "pointer:generic ft5x06 (11)"
    Option "CalibrationMatrix" "0 -1 1 1 0 0 0 0 1"
EndSection

Section "Monitor"
    Identifier "DSI-1"
    Option "Rotate" "left"
EndSection
"""

square_right = """
Section "InputClass"
    Identifier "libinput HyperPixel4 Square"
    MatchProduct "pointer:generic ft5x06 (11)"
    Option "CalibrationMatrix" "0 1 0 -1 0 1 0 0 1"
EndSection

Section "Monitor"
    Identifier "DSI-1"
    Option "Rotate" "right"
EndSection
"""

square_default = """
Section "InputClass"
    Identifier "libinput HyperPixel4 Square"
    MatchProduct "pointer:generic ft5x06 (11)"
    Option "CalibrationMatrix" "1 0 0 0 1 0 0 0 1"
EndSection

Section "Monitor"
    Identifier "DSI-1"
    Option "Rotate" "default"
EndSection
"""

square_inverted = """
Section "InputClass"
    Identifier "libinput HyperPixel4 Square"
    MatchProduct "pointer:generic ft5x06 (11)"
    Option "CalibrationMatrix" "-1 0 1 0 -1 1 0 0 1"
EndSection

Section "Monitor"
    Identifier "DSI-1"
    Option "Rotate" "inverted"
EndSection
"""

orientations = {
    1: ('left', 'left'),
    2: ('right', 'right'),
    3: ('default', 'default'),
    4: ('inverted', 'inverted')
}

def persist():
    print("Select display type:")
    print("[1] Rectangle")
    print("[2] Square")
    
    display_type_choice = input("Enter your choice (1 or 2): ").strip()

    if display_type_choice == '1':
        display_type = 'rectangle'
    elif display_type_choice == '2':
        display_type = 'square'
    else:
        print("Invalid display type. Please choose either '1' for square or '2' for rectangle.")
        return

    print("Select orientation:")
    for num, (key, _) in orientations.items():
        print(f"[{num}] {key.capitalize()}")
    
    try:
        orientation_choice = int(input("Enter your choice (1-4): ").strip())
        if orientation_choice not in orientations:
            print("Invalid orientation. Please choose a number between 1 and 4.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    orientation, _ = orientations[orientation_choice]
    
    config = ""

    if display_type == 'rectangle':
        if orientation == 'left':
            config = rectangle_left
        elif orientation == 'right':
            config = rectangle_right
        elif orientation == 'default':
            config = rectangle_default
        elif orientation == 'inverted':
            config = rectangle_inverted
    elif display_type == 'square':
        if orientation == 'left':
            config = square_left
        elif orientation == 'right':
            config = square_right
        elif orientation == 'default':
            config = square_default
        elif orientation == 'inverted':
            config = square_inverted

    config_file_path = '/usr/share/X11/xorg.conf.d/88-hyperpixel4.conf'
    try:
        with open(config_file_path, 'w') as config_file:
            config_file.write(config)
        print(f"Configuration written to {config_file_path}")
    except PermissionError:
        print("Permission denied. Please run the script as root or with sudo.")
    except Exception as e:
        print(f"An error occurred: {e}")

persist()