from gpiozero import LED, Button, Buzzer, PWMLED
import time
# gpiozero does not require setting pin modes # Use BCM numbering
led = LED(14) # Set GPIO 14 as an output
# Main program loop
print("Starting basic output control. Press Ctrl+C to stop.")
while True:
    print("Setting GPIO 14 HIGH (ON)")
    led.on() # Turn the LED ON
    time.sleep(1)           # Wait for 1 second
    print("Setting GPIO 14 LOW (OFF)")
    led.off() # Turn the device OFF
    time.sleep(1)           # Wait for 1 second