import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 16
photo = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(photo, GPIO.IN)

while True:
    time.sleep(0.01)
    GPIO.output(16, not GPIO.input(photo))