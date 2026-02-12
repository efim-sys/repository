import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 17
btn = 13

GPIO.setup(led, GPIO.OUT)
GPIO.setup(btn, GPIO.IN)

while True:
    time.sleep(0.2)
    if(GPIO.input(btn)):
        GPIO.output(led, not GPIO.input(led))