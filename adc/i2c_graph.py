import i2c10_driver
import RPi.GPIO as GPIO
import time
from matplotlib import pyplot
import os

tt = 10 # sec


os.system("raspi-gpio set 2 a0")
os.system("raspi-gpio set 3 a0")

dac = i2c10_driver.MCP3021(3.3)


t_list = []
v_list = []

for i in range(int(tt/0.01)):
    v = dac.getvoltage()
    # print(f'Voltage = {bin(v_b)} -> {(v_b/255) * v_max}')
    time.sleep(0.01)
    t_list.append(i*0.01)
    v_list.append(v)
    print(f'\r{i/int(tt/0.01)*100.0}%', end="")

pyplot.figure(figsize=(10, 6))
pyplot.plot(t_list, v_list)

pyplot.show()
