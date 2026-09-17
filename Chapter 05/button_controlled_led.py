from gpiozero import LED, Button
from time import sleep
led = LED(14)
button = Button(21)
print("Monitoring button and controlling LED... Press Ctrl+C to stop.")
while True:
    if button.is_pressed:
        led.on()
        print("Button Pressed  →  LED ON")
    else:
        led.off()
        print("Button Released  →  LED OFF")
    sleep(0.1)