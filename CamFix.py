import os
import time
import ctypes
import keyboard

print("Loading Libraries ...")

# Measure the execution time
start_time = time.perf_counter()

# Windows API Constants
WM_HOTKEY = 0x0312
MOD_CTRL = 0x0002
MOD_SHIFT = 0x0004

# Keybind for 'CTRL + SHIFT + C'
KEYBIND = 'ctrl+shift+c'

# File path
file_path = "CamFix.txt"

# Load user32 library
user32 = ctypes.windll.user32

# Structure for POINT
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long),
                ("y", ctypes.c_long)]

# Function to move the cursor
def move_cursor(x, y):
    point = POINT(x, y)
    user32.SetCursorPos(x, y)

# Function to get the initial timestamp of the file
def get_initial_timestamp():
    return os.path.getmtime(file_path)

# Wait for the CamFix.txt file to be created
end_time = time.perf_counter()
print("Loading Libraries took", end_time - start_time, "seconds")
print("Loaded Libraries!")
print("Waiting for CamFix.txt")
while not os.path.isfile(file_path):
    time.sleep(0)
print("CamFix.txt found!")

# Initialize variables
on = False
x, y = None, None
initial_timestamp = get_initial_timestamp()

# Register the keybind handler
keyboard.add_hotkey(KEYBIND, lambda: keyboard.press('esc'))

# Main loop
while True:
    current_timestamp = get_initial_timestamp()

    # Check if the file has been updated
    if current_timestamp > initial_timestamp:
        print("File updated.")

        with open(file_path, "r") as file:
            contents = file.readlines()

        # Extract values from the file
        if contents[0] == "true\n":
            cord = contents[1].split(" ")
            x = int(cord[0])
            y = int(cord[1])
            on = True
        else:
            on = False

        print(contents[0])
        print(x)
        print(y)

        initial_timestamp = current_timestamp

    # Check if the keybind is pressed to exit the code
    if keyboard.is_pressed('f10'):
        print("Exiting...")
        break

    # Move the cursor if the 'on' flag is True
    if on:
        move_cursor(x, y)

    time.sleep(0)
