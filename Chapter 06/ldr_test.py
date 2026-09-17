from gpiozero import LightSensor
from time import sleep

# Define the GPIO pin connected to the LDR and Capacitor (BCM numbering)
LDR_PIN = 14

# Create the LightSensor object
# charge_time_limit: Sets the maximum time the library will wait for the capacitor to charge.
# 0.1s is appropriate for a 10µF capacitor in this setup.
sensor = LightSensor(LDR_PIN, charge_time_limit=0.1) 

print("LDR Test (Light Sensor). Press Ctrl+C to exit.")

# Main loop to continuously read light intensity
while True:
    # 'value' property returns a normalized reading between 0.0 (Dark) and 1.0 (Bright)
    light_value = sensor.value
    
    print(f"Light Intensity: {light_value:.2f} (0.0=Dark, 1.0=Bright)")
    
    sleep(0.5) # Read every half second