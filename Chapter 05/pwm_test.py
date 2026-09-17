from gpiozero import PWMLED
from time import sleep
led = PWMLED(18)
print("Fading LED... Press Ctrl+C to stop.")
while True:
    # Fade in
    for i in range(0, 101, 5):
        led.value = i / 100
        print(f"Brightness: {i}%")
        sleep(0.1)
    sleep(0.5)
    # Fade out
    for i in range(100, -1, -5):
        led.value = i / 100
        print(f"Brightness: {i}%")
        sleep(0.1)
    sleep(0.5)