# log_data_manual.py
import time # To get timestamps

sensor_value = 28.3 # Example reading

# Open file in append mode ('a')
# If sensor_log.txt doesn't exist, it will be created.
# If it exists, new data is added to the end.
log_file = open("sensor_log.txt", "a")

# Get current time (simple example)
timestamp = time.ctime() # Gets a formatted time string

# Prepare the log entry string - IMPORTANT: add newline \n
log_entry = timestamp + " - Sensor Value: " + str(sensor_value) + "\n"

# Write the entry to the file
log_file.write(log_entry)
print("Logged:", log_entry.strip()) # Print without the newline

# IMPORTANT: Close the file to ensure data is saved
log_file.close()
print("Log file closed.")