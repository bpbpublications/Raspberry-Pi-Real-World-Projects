
import time
from Adafruit_IO import MQTTClient
import board
import digitalio

# --- Adafruit IO Configuration ---
# IMPORTANT: Replace these placeholders with your actual Adafruit IO credentials
ADAFRUIT_IO_USERNAME = 'YOUR_AIO_USERNAME'
ADAFRUIT_IO_KEY = 'YOUR_AIO_KEY'

# Define Feeds for each light switch. These must exist in your Adafruit IO account.
LIGHT_FEEDS = {
    'light-1': 'light-1-control',
    'light-2': 'light-2-control',
    'light-3': 'light-3-control',
    'light-4': 'light-4-control'
}

# --- Hardware Configuration ---
# Map the light names to their corresponding CircuitPython Board Pins
LIGHT_PINS = {
    'light-1': board.D12, # Changed from D26 to D12
    'light-2': board.D20,
    'light-3': board.D21,
    'light-4': board.D16
}

# Dictionary to hold the digitalio control objects
light_control_objects = {}

# --- Setup ---
print("Initializing GPIO Pins...")
try:
    for light_name, pin_id in LIGHT_PINS.items():
        pin = digitalio.DigitalInOut(pin_id)
        pin.direction = digitalio.Direction.OUTPUT
        pin.value = False # Initialize all lights OFF
        light_control_objects[light_name] = pin
        print(f"Initialized {light_name} on {pin_id}.")
except Exception as e:
    print(f"Error setting up GPIO: {e}")
    exit(1)

# --- MQTT Callback Functions ---
def connected(client):
    """Callback function called when the client is connected to Adafruit IO."""
    print("Connected to Adafruit IO! Listening for lighting commands...")
    # Subscribe to ALL light control feeds to receive commands
    for feed_name in LIGHT_FEEDS.values():
        client.subscribe(feed_name)
        print(f"Subscribed to feed: {feed_name}")

def disconnected(client):
    """Callback function called when the client disconnects."""
    print("Disconnected from Adafruit IO!")

def message(client, feed_id, payload):
    """Callback function called when a message is received from the cloud."""
    print(f"Received command on {feed_id}: {payload}")
    # 1. Determine which light name (e.g., 'light-1') corresponds to the feed_id
    light_name = None
    for name, fid in LIGHT_FEEDS.items():
        if fid == feed_id:
            light_name = name
            break
    if light_name is None:
        print(f"Error: Unknown feed ID {feed_id}")
        return
    # 2. Get the digitalio object for that light
    pin_object = light_control_objects.get(light_name)
    # 3. Process the command (payload)
    if payload == 'ON':
        pin_object.value = True
        print(f"--> {light_name.capitalize()} switched ON. Listen for relay click!")
    elif payload == 'OFF':
        pin_object.value = False
        print(f"--> {light_name.capitalize()} switched OFF.")
    else:
        print("Invalid command received.")

# --- Main Program Execution ---
# Initialize MQTT client
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Assign callback functions
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

# Connect to the Adafruit IO broker
try:
    print("Attempting to connect to Adafruit IO...")
    client.connect()
    # Start the network loop in the background to continuously listen for messages
    client.loop_background()
except Exception as e:
    print(f"Error connecting to Adafruit IO: {e}. Cannot control remotely.")

print("Starting Remote Lighting Control System. Check dashboard for control.")
try:
    # The main loop simply keeps the script alive while the MQTT loop handles commands
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nProgram stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Cleanly disconnect MQTT client
    client.disconnect()
    # Explicitly deinitialize all GPIO resources
    for pin_object in light_control_objects.values():
        pin_object.deinit()
    print("GPIO resources explicitly released and MQTT disconnected.")
