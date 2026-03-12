import r2r_driver
import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

tt = 3 # sec

PIN_CMP = 21
v_max = 3.3

dac = r2r_driver.R2R_DAC([11, 25, 12, 13, 16, 19, 20, 26], 255)

GPIO.setup(PIN_CMP, GPIO.IN)

def measure():
    for i in range(256):
        dac.setbyte(i)
        # time.sleep(1e-6)
        if GPIO.input(PIN_CMP):
            return i
    return 255

periods = []

for i in range(int(tt/0.01)):
    start = time.perf_counter()
    v = measure()/255*v_max
    finish = time.perf_counter()
    # print(f'Voltage = {bin(v_b)} -> {(v_b/255) * v_max}')
    time.sleep(0.01)
    periods.append(finish - start)
    print(f'\r{i/int(tt/0.01)*100.0}%', end="")

pyplot.figure(figsize=(10, 8))
pyplot.hist(periods)


pyplot.show()
