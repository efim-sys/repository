import pwm_dac_driver

if __name__ == "__main__":
    dac = pwm_dac_driver.PWM_DAC(12, 3.3)

    try:
        
        try:
            while True:
                v = float(input("Input voltage: "))
                dac.setvoltage(v)

        except ValueError:
            print("Error... enter voltage again")

    finally:
        dac.deinit()
