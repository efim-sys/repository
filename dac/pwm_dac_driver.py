import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio, vmax):
        self.gpio = gpio
        self.vmax = vmax

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.gpio, GPIO.OUT, initial = 0)
        self.pwm = GPIO.PWM(gpio, 1000)

        self.pwm.start(0.0)

    def deinit(self):
        self.pwm.stop()
        GPIO.output(self.gpio, 0)
        GPIO.cleanup()

    def setvoltage(self, v):
        if(not (0 <= v <= self.vmax)):
            print(f"Voltage out of range [0.0v - {self.vmax}v]")
            return 0
        self.pwm.ChangeDutyCycle(v/self.vmax*100.0)
    