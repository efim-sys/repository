import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

for led in leds:
    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, 0)
