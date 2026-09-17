
#!/usr/bin/env python3
# environmental_control.py
# Read BME280 (I2C) data and publish to Adafruit IO; subscribe to pump control feed.
# Requires: adafruit-blinka, adafruit-circuitpython-bme280, adafruit-io, gpiozero

import time
import board
import busio
import adafruit_bme280.advanced as adafruit_bme280
from Adafruit_IO import MQTTClient
from gpiozero import LED

# --- Adafruit IO Configuration (replace with your credentials) ---
ADAFRUIT_IO_USERNAME = 'YOUR_AIO_USERNAME'
ADAFRUIT_IO_KEY = 'YOUR_AIO_KEY'

# Feed names (must match feeds created on Adafruit IO)
HUMIDITY_FEED = 'ambient-humidity'
TEMPERATURE_FEED = 'ambient-temperature'
PRESSURE_FEED = 'ambient-pressure'
PUMP_CONTROL_FEED = 'manual-control' # expects 'ON' / 'OFF' strings

# --- Hardware setup ---
# I2C for BME280 (SCL = GPIO3, SDA = GPIO2)
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
bme280.sea_level_pressure = 1013.25 # optional, adjust to local sea-level pressure

# Relay control (use gpiozero LED class as a simple digital output)
# Ensure this pin matches your wiring (BCM 23 -> board pin 16)
pump_relay = LED(23)
pump_relay.off() # ensure pump is off at start

# --- MQTT callbacks and helpers ---
def water_plant(duration=5):
    """Run pump for given duration (seconds)."""
    print(f"--> Activating pump for {duration} s")
    pump_relay.on()
    time.sleep(duration)
    pump_relay.off()
    print("--> Pump deactivated")

def connected(client):
    print("Connected to Adafruit IO. Subscribing to control feed...")
    try:
        client.subscribe(PUMP_CONTROL_FEED)
    except Exception as e:
        print("Subscription failed:", e)

def disconnected(client):
    print("Disconnected from Adafruit IO")

def message(client, feed_id, payload):
    print(f"Message received on {feed_id}: {payload}")
    if feed_id == PUMP_CONTROL_FEED:
        payload = str(payload).upper().strip()
        if payload == 'ON':
            water_plant()
            # Optionally publish 'OFF' back to reset a remote toggle/button
            try:
                client.publish(PUMP_CONTROL_FEED, 'OFF')
            except Exception:
                pass
        elif payload == 'OFF':
            print("Received OFF command; no action required.")
        else:
            print("Unknown payload:", payload)

# --- Main program ---
client = None
try:
    client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
    client.on_connect = connected
    client.on_disconnect = disconnected
    client.on_message = message
    print("Connecting to Adafruit IO...")
    client.connect()
    client.loop_background()
except Exception as e:
    print(f"Could not connect to Adafruit IO: {e}. Continuing in local-only mode.")

print("Starting environmental monitor (Ctrl+C to stop)")
try:
    while True:
        # Read sensor values with defensive handling
        try:
            temperature = bme280.temperature
            humidity = bme280.humidity
            pressure = bme280.pressure
        except Exception as e:
            print("Sensor read error:", e)
            temperature = humidity = pressure = None
        if temperature is not None and humidity is not None and pressure is not None:
            print(f"Temp={temperature:.1f} °C \n Humidity={humidity:.1f}% \n Pressure={pressure:.1f} hPa")
            # Publish to Adafruit IO (protected by try/except)
            if client is not None:
                try:
                    client.publish(HUMIDITY_FEED, f"{humidity:.1f}")
                    client.publish(TEMPERATURE_FEED, f"{temperature:.1f}")
                    client.publish(PRESSURE_FEED, f"{pressure:.1f}")
                    print("Published data to Adafruit IO")
                except Exception as e:
                    print("Publish failed:", e)
        else:
            print("Failed to read BME280 sensor data. Check wiring and I2C.")
        time.sleep(10) # delay between readings (avoid rate limits)
except KeyboardInterrupt:
    print("\nStopping by user request")
except Exception as e:
    print("Unexpected error:", e)
finally:
    # Ensure hardware is left in a safe state
    try:
        pump_relay.off()
    except Exception:
        pass
    # Disconnect MQTT if available
    try:
        if client is not None:
            client.disconnect()
    except Exception:
        pass
    print("Clean shutdown complete.")
