import r2r_driver

if __name__ == "__main__":
    dac = r2r_driver.R2R_DAC([22,27,17,26,25,21,20,16], 3.005)

    try:
        
        try:
            while True:
                v = float(input("Input voltage: "))
                dac.setvoltage(v)

        except ValueError:
            print("Error... enter voltage again")

    finally:
        dac.deinit()
