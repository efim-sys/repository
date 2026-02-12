import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 16

GPIO.setup(led, GPIO.OUT)

while True:
    time.sleep(0.2)
    GPIO.output(led, not GPIO.input(led))