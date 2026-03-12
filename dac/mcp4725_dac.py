import mcp4725_driver

import os

os.system("raspi-gpio set 2 a0")
os.system("raspi-gpio set 3 a0")

if __name__ == "__main__":
    dac = mcp4725_driver.MCP4725(4.242, verbose=True)

    try:
        
        try:
            while True:
                v = float(input("Input voltage: "))
                dac.setvoltage(v)

        except ValueError:
            print("Error... enter voltage again")

    finally:
        dac.deinit()
