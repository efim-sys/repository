import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio, vmax):
        self.gpio = gpio
        self.vmax = vmax

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.gpio, GPIO.OUT, initial = 0)

    def deinit(self):
        GPIO.output(self.gpio, 0)
        GPIO.cleanup()

    def setbyte(self, byte):
        for i in range(8):
            mask = 1 << i
            GPIO.output(self.gpio[i], byte & mask)

    def setvoltage(self, v):
        if(not (0 <= v <= self.vmax)):
            print(f"Voltage {v} out of range [0.0v - {self.vmax}v]")
            return 0
        self.setbyte(int(v/self.vmax * 255))