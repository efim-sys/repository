import r2r_driver
import RPi.GPIO as GPIO
import time

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

while(True):
    v_b = measure()
    print(f'Voltage = {bin(v_b)} -> {(v_b/255) * v_max}')
    time.sleep(1)
