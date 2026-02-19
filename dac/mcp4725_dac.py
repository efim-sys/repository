import mcp4725_driver

if __name__ == "__main__":
    dac = mcp4725_driver.MCP4725(3.3, verbose=True)

    try:
        
        try:
            while True:
                v = float(input("Input voltage: "))
                dac.setvoltage(v)

        except ValueError:
            print("Error... enter voltage again")

    finally:
        dac.deinit()
