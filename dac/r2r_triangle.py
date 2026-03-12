import r2r_driver as r2r
import math
import time

amplitude = 1.5
freq = 100
sampling_freq = 10000

dac = r2r.R2R_DAC([22,27,17,26,25,21,20,16], 3.005)

try:
    while(True):
        t = time.time_ns()/1000000000

        val = abs(math.fmod(t, 1/freq) - 0.5/freq)*2*amplitude*freq

        dac.setvoltage(val)
        
        time.sleep(1/sampling_freq)

finally:
    dac.deinit()