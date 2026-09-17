from gpiozero import Buzzer
from time import sleep
# Create a Buzzer object on BCM pin 21
buzzer = Buzzer(21)
print("Controlling buzzer on BCM pin 21. Press Ctrl+C to stop.")
# Turn the buzzer ON
buzzer.on()
print("Buzzer ON (sounding)...")
sleep(1)  # Keep it ON for 1 second
# Turn the buzzer OFF
buzzer.off()
print("Buzzer OFF (silent).")