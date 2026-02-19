import pwm_dac_driver
import math
import time

amplitude = 1.5
freq = 10
sampling_freq = 10000

dac = pwm_dac_driver.PWM_DAC(12, 3.3)

try:
    while(True):
        t = time.time_ns()/1000000000

        val = abs(math.fmod(t, 1/freq) - 0.5/freq)*2*amplitude*freq

        dac.setvoltage(val)
        
        time.sleep(1/sampling_freq)

finally:
    dac.deinit()