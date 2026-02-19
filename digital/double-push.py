import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

up = 9
down = 10

for led in leds:
    GPIO.setup(led, GPIO.OUT)

GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

def setbyte(byte):
    for i in range(8):
        mask = 1 << i
        GPIO.output(leds[i], byte & mask)

byte = 0
setbyte(byte)

while True:
    delta = 0
    while(delta == 0):
        up_val = GPIO.input(up)
        down_val = GPIO.input(down)
        
        delta += up_val
        delta -= down_val

        if(up_val and down_val):
            delta = 1
            byte = 254

        time.sleep(0.01)

    byte = (byte+delta) % 256
    setbyte(byte)

    time.sleep(0.4)