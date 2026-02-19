import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

r2r = list(reversed([16, 20, 21, 25, 26, 17, 27, 22]))

for r in r2r:
    GPIO.setup(r, GPIO.OUT)


def setbyte(byte):
    for i in range(8):
        mask = 1 << i
        GPIO.output(r2r[i], byte & mask)

vmax = 3.3

def voltage2num(v):
    if(not (0 <= v <= vmax)):
        print(f"Voltage out of range [0.0v - {vmax}v]")
        return 0
    return int(v/vmax * 255)

try:
    try:
        while True:
            v = float(input("Input voltage: "))
            num = voltage2num(v)
            print(f"[Degub] bin = {bin(num)}")
            setbyte(num)

    except ValueError:
        print("Error... enter voltage again")

finally:
    GPIO.output(r2r, 0)
    GPIO.cleanup()
