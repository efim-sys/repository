import mcp4725_driver
import math
import time

amplitude = 1.5
freq = 100
sampling_freq = 100000

dac = mcp4725_driver.MCP4725(4.2)

try:
    while(True):
        t = time.time_ns()/1000000000

        val = abs(math.fmod(t, 1/freq) - 0.5/freq)*2*amplitude*freq

        dac.setvoltage(val)
        
        time.sleep(1/sampling_freq)

finally:
    dac.deinit()