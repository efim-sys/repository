import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

for led in leds:
    GPIO.setup(led, GPIO.OUT)

for led in leds:
    GPIO.output(led, 0)

while True:
    for led in leds:
        GPIO.output(led, 1)
        time.sleep(0.1)
        GPIO.output(led, 0)

    for led in reversed(leds):
        GPIO.output(led, 1)
        time.sleep(0.1)
        GPIO.output(led, 0)