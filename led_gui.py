import RPi.GPIO as GPIO
import tkinter as tk

# Define LED GPIO pins
LED_RED = 17
LED_GREEN = 18
LED_BLUE = 27

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_RED, GPIO.OUT)
GPIO.setup(LED_GREEN, GPIO.OUT)
GPIO.setup(LED_BLUE, GPIO.OUT)

# Function to turn off all LEDs
def turn_off_all():
    GPIO.output(LED_RED, GPIO.LOW)
    GPIO.output(LED_GREEN, GPIO.LOW)
    GPIO.output(LED_BLUE, GPIO.LOW)

# Function to handle radio button clicks
def select_led(led_pin):
    turn_off_all()  # Turn off all LEDs
    GPIO.output(led_pin, GPIO.HIGH)  # Turn on the selected LED

# Create the GUI
root = tk.Tk()
root.title("LED Controller")

# Radio buttons
red_button = tk.Radiobutton(root, text="Red LED", command=lambda: select_led(LED_RED))
red_button.pack(anchor=tk.W)

green_button = tk.Radiobutton(root, text="Green LED", command=lambda: select_led(LED_GREEN))
green_button.pack(anchor=tk.W)

blue_button = tk.Radiobutton(root, text="Blue LED", command=lambda: select_led(LED_BLUE))
blue_button.pack(anchor=tk.W)

# Exit button
exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

# Run the GUI
root.mainloop()

# Cleanup GPIO
GPIO.cleanup()
