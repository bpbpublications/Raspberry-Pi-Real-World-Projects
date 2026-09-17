from gpiozero import DistanceSensor, LED, Buzzer, DigitalInputDevice
from time import sleep

# --- GPIO Pin Definitions (BCM numbering) ---
# HC-SR04 Ultrasonic Sensor (Trigger=23, Echo=24)
sensor = DistanceSensor(echo=24, trigger=23, max_distance=4) 
# Touch Sensor (Input=17)
touch_sensor = DigitalInputDevice(17)
# Output Devices (Buzzer=27, LED=22)
buzzer = Buzzer(27)
led = LED(22)

# --- System Configuration ---
DISTANCE_THRESHOLD_CM = 50 
print("Smart Doorbell/Security System Active (gpiozero). Press Ctrl+C to stop.")

# Main loop for the system
while True:
    # The 'distance' property returns distance in meters
    distance_m = sensor.distance
    distance_cm = distance_m * 100
    
    # --- Proximity Detection ---
    if distance_cm > 2 and distance_cm < DISTANCE_THRESHOLD_CM:
        print(f"Intruder/Visitor Detected! Distance: {distance_cm:.2f} cm")
        
        # --- Doorbell/Security Logic ---
        if touch_sensor.is_active:
            print("Doorbell Pressed! ALARM.")
            buzzer.on()
            led.on()
            sleep(1) # Buzzer/LED active for 1 second
            buzzer.off()
            led.off()
            sleep(2) # Short delay to prevent immediate re-triggering of doorbell
        else:
            # If no touch, just a proximity alert (flash LED)
            print("Proximity Alert!")
            led.blink(on_time=0.2, off_time=0.2, n=3) # Flash 3 times
            sleep(1.5) # Wait for flash cycle to complete
    
    else:
        # No proximity detected
        buzzer.off()
        led.off()
        
    sleep(0.5) # Short delay for main loop iteration