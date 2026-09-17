from gpiozero import Button
from time import sleep
button = Button(15)
print("Reading GPIO 15 state... Press Ctrl+C to stop.")
try:
    while True:
        if button.is_pressed:
            print("Button Pressed (LOW state)")
        else:
            print("Button Released (HIGH state)")
        sleep(0.5)  # Small delay to prevent excessive CPU usage
except KeyboardInterrupt:
    print("Program stopped by user.")