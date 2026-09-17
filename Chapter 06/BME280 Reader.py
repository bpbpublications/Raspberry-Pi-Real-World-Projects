import time
import board
import busio
import adafruit_bme280

# Create I2C bus
# Assumes I2C is enabled and SDA/SCL pins are connected correctly
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor object
# The default I2C address (0x77 or 0x76) is handled by the library
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Optional: set sea level pressure for accurate altitude readings (typical value)
bme280.sea_level_pressure = 1013.25

print("Reading BME280 sensor...")

while True:
    print(f"Temperature: {bme280.temperature:.1f} °C")
    print(f"Humidity: {bme280.humidity:.1f} %")
    print(f"Pressure: {bme280.pressure:.1f} hPa")
    
    time.sleep(2)