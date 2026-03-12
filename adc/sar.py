import r2r_driver
import RPi.GPIO as GPIO
import time

PIN_CMP = 21
v_max = 3.3

dac = r2r_driver.R2R_DAC([11, 25, 12, 13, 16, 19, 20, 26], 255)

GPIO.setup(PIN_CMP, GPIO.IN)

def measure():
    bitmask = 0b10000000

    number = 0
    step = 0
    while bitmask:
        number = number | bitmask
        dac.setbyte(number)
        
        print(f'step={step} num={number:08b} bitmask={bitmask:08b}')
        
        if GPIO.input(PIN_CMP):
            number = number ^ bitmask

        bitmask >>= 1

        step+=1

        # time.sleep(1)

    return number


while(True):
    v_b = measure()
    print(f'\rVoltage = {v_b:08b} -> {((v_b/255) * v_max):.2f}', end = "")
    time.sleep(0.1)
