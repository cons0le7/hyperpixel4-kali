import os
import sys
import subprocess

instructions = """
To make rotation settings stay after reboot / power off:

[1] Tap the blue kali icon at the top left of desktop
[2] Navigate to: Settings > Settings Manager > Session and Startup > Application Autostart
[3] Click "Add"
[4] Set a name and description.
[5] Set trigger to ‘on login’
For the command field copy and paste this line:

"""

rect_left = "/home/kali/hyperpixel4-kali/rectangular-rotos/left.sh"
rect_right = "/home/kali/hyperpixel4-kali/rectangular-rotos/right.sh"
rect_default = "/home/kali/hyperpixel4-kali/rectangular-rotos/default.sh"
rect_inverted = "/home/kali/hyperpixel4-kali/rectangular-rotos/inverted.sh"

square_left = "/home/kali/hyperpixel4-kali/square-rotos/left.sh"
square_right = "/home/kali/hyperpixel4-kali/square-rotos/right.sh"
square_default = "/home/kali/hyperpixel4-kali/square-rotos/default.sh"
square_inverted = "/home/kali/hyperpixel4-kali/square-rotos/inverted.sh"

def persist_rectangle():
    rectangle_roto = int(input("""
Select Orientation: 
[1] Left 
[2] Right 
[3] Default 
[4] Inverted 
[5] Exit 
"""))
    if rectangle_roto == 1:
        print(instructions)
        print(rect_left)
        print("\nsudo reboot after saving and log in to ensure changes take effect.")
    elif rectangle_roto == 2:
        print(instructions)
        print(rect_right)
        print("\nsudo reboot after saving and log in to ensure changes take effect.")
    elif rectangle_roto == 3:
        print(instructions)
        print(rect_default)
        print("\nsudo reboot after saving and log in to ensure changes take effect.")
    elif rectangle_roto == 4:
        print(instructions)
        print(rect_inverted)
        print("\nsudo reboot after saving and log in to ensure changes take effect.")
    elif rectangle_roto == 5:
        sys.exit()
    else:
        print("Invalid input. Enter a number 1-5.")
        persist_rectangle()

def persist_square():
    square_roto = int(input("""
Select Orientation: 
[1] Left 
[2] Right 
[3] Default 
[4] Inverted 
[5] Exit 
"""))
    if square_roto == 1:
        print(instructions)
        print(square_left)
        print("sudo reboot after saving and log in to ensure changes take effect.")
    elif square_roto == 2:
        print(instructions)
        print(square_right)
        print("sudo reboot after saving and log in to ensure changes take effect.")
    elif square_roto == 3:
        print(instructions)
        print(square_default)
        print("sudo reboot after saving and log in to ensure changes take effect.")
    elif square_roto == 4:
        print(instructions)
        print(square_inverted)
        print("sudo reboot after saving and log in to ensure changes take effect.")
    elif square_roto == 5:
        sys.exit()
    else:
        print("Invalid input. Enter a number 1-5.")
        persist_square()

def persist_menu():
    display = int(input("""
Select display type: 
[1] Rectangular 
[2] Square 
[3] Exit
"""))
    if display == 1:
        persist_rectangle()
    elif display == 2:
        persist_square()
    elif display == 3:
        sys.exit()
    else:
        print("Invalid input. Enter a number 1-3.")
        persist_menu()

def install():
    commands = [
        "cd /home/kali/hyperpixel4-kali && chmod +x hyperpixel4-kali.sh && chmod +x rotation.sh",
        "chmod +x /home/kali/hyperpixel4-kali/rectangular-rotos/*.sh",
        "chmod +x /home/kali/hyperpixel4-kali/square-rotos/*.sh",
        "./hyperpixel4-kali.sh",
        "curl -sSL https://get.pimoroni.com/hyperpixel4-legacy | bash"
    ]

    for command in commands:
        print(f"Running command: {command}")
        result = subprocess.run(command, shell=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Error: {result.stderr}")

def edit_config():
    file = '/boot/config.txt'
    append = 'dtoverlay=vc4-fkms-v3d\n'
    try:
        with open(file, 'r') as f:
            lines = f.readlines()
        if append not in lines:
            with open(file, 'a') as f:
                f.write(append)
            print(f"The line '{append.strip()}' has been added to '{file}'.")
            print("\nSetup Complete. \nExiting...")
            sys.exit()
        else:
            print(f"The line '{append.strip()}' is already present in '{file}'.")
    except PermissionError:
        print("Permission denied.")
    except FileNotFoundError:
        print(f"The file '{file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def menu():
    print("""                                                                                
██╗  ██╗██████╗ ██╗  ██╗      ██╗  ██╗ █████╗ ██╗     ██╗
██║  ██║██╔══██╗██║  ██║      ██║ ██╔╝██╔══██╗██║     ██║
███████║██████╔╝███████║█████╗█████╔╝ ███████║██║     ██║
██╔══██║██╔═══╝ ╚════██║╚════╝██╔═██╗ ██╔══██║██║     ██║
██║  ██║██║          ██║      ██║  ██╗██║  ██║███████╗██║
╚═╝  ╚═╝╚═╝          ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝                                                                       
    """)
    choice = int(input("""
x-----------------------------------------------------x
|---[HyperPixel 4.0 driver install for Kali 2024.3]---|
|-----------------------------------------------------|
| [1] | Install                                       |
| [2] | Update Config                                 |
| [3] | Rotate Display                                |
| [4] | Setup Persistence                             |
| [5] | Exit                                          |
|-----------------------------------------------------|
|---[https://github.com/cons0le7/hyperpixel4-kali]----|
x-----------------------------------------------------x
"""))
    if choice == 1:
        install()
    elif choice == 2:
        edit_config()
    elif choice == 3:
        import rotate
    elif choice == 4:
        persist_menu()
    elif choice == 5:
        sys.exit()
    else:
        print("Invalid input. Enter a number 1-5.")
        menu()

menu()