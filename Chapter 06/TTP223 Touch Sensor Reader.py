from gpiozero import DigitalInputDevice
from time import sleep

# Define the GPIO pin connected to the touch sensor's signal output
# GPIO 14 is used here, ensure it matches your wiring (BCM numbering)
TOUCH_SENSOR_PIN = 14 

# Create a DigitalInputDevice object. This configures the pin as a digital input.
# We do not need a pull-up or pull-down resistor here because the sensor module handles the stable state.
touch_sensor = DigitalInputDevice(TOUCH_SENSOR_PIN)

print("Touch sensor setup complete. Waiting for touch... Press Ctrl+C to stop.")

# Main loop to continuously read the sensor state
while True:
    # The 'is_active' property returns True if the pin is HIGH (active state)
    if touch_sensor.is_active:
        print("Touch Detected!")
    else:
        print("No Touch")
    
    sleep(0.5) # Wait for 0.5 seconds before reading again