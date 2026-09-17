from gpiozero import DistanceSensor
from time import sleep

# Define GPIO pins for Trigger and Echo (BCM numbering)
# NOTE: A voltage divider MUST be used on the ECHO_PIN (15) to protect the Pi's GPIO
TRIG_PIN = 14
ECHO_PIN = 15

# Create the DistanceSensor object. 
# max_distance=4 sets the maximum range to 4 meters.
sensor = DistanceSensor(echo=ECHO_PIN, trigger=TRIG_PIN, max_distance=4)

print("HC-SR04 Distance Measurement Test (gpiozero). Press Ctrl+C to stop.")

# Main loop to continuously measure distance
while True:
    # The 'distance' property gives the measurement in meters (0.0 to max_distance)
    distance_m = sensor.distance
    
    # Convert distance to centimeters for the required output
    distance_cm = distance_m * 100
    
    # Check if the measurement is within the sensor's effective range (2cm to 400cm)
    if distance_cm > 2 and distance_cm < 400:
        print(f"Distance: {distance_cm:.2f} cm")
    else:
        # Indicate if the object is too close, too far, or no valid echo was received
        print("Object out of effective range (2-400cm) or no valid echo detected.")
        
    sleep(1) # Wait 1 second before the next measurement