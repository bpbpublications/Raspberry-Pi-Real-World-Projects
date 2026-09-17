from gpiozero import Buzzer, Button
from time import sleep
buzzer = Buzzer(14)
button = Button(21)
print("Monitoring button and controlling buzzer... Press Ctrl+C to stop.")
while True:
    if button.is_pressed:
        buzzer.on()
        print("Button Pressed → Alarm ON")
    else:
        buzzer.off()
        print("Button Released → Alarm OFF")
    sleep(0.1)