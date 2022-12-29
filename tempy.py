import time
import subprocess
import datetime
import os

def get_voltage():
  output = subprocess.run(["vcgencmd", "measure_volts"], capture_output=True).stdout.decode().strip()
  return output

def get_temperature():
  output = subprocess.run(["vcgencmd", "measure_temp"], capture_output=True).stdout.decode().strip()
  return output

with open("voltage_temperature.log", "a") as log_file:
  while True:
    voltage = get_voltage()
    temperature = get_temperature()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    output = f"[{current_time}] Voltage: {voltage} | Temperature: {temperature}"
    print(f"\r{output}", end="")
    log_file.write(f"{output}\n")
    log_file_size = os.stat("voltage_temperature.log").st_size
    if log_file_size > 30 * 1024 * 1024:
      log_file.close()
      log_file = open("voltage_temperature.log", "w")
    time.sleep(1)
