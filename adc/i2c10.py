import i2c10_driver
import time
import os

os.system("raspi-gpio set 2 a0")
os.system("raspi-gpio set 3 a0")

dac = i2c10_driver.MCP3021(3.3)

while True:
    print(dac.getvoltage())
    time.sleep(0.1)