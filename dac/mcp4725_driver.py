import smbus

class MCP4725:
    def __init__(self, vmax, address = 0x61, verbose = False):
        self.bus = smbus.SMBus(1)

        self.address = address
        self.wm = 0x00
        self.pds = 0x00
        self.verbose = verbose
        self.vmax = vmax
    
    def deinit(self):
        self.bus.close()

    def setnum(self, num):
        if not isinstance(num, int):
            print("Only integers")
            return
        
        if not (0 <= num <= 4095):
            print("number out of range")
            return
        
        first_byte = self.wm | self.pds | (num >> 8)
        second_byte = num & 0xff

        self.bus.write_byte_data(self.address, first_byte, second_byte)

        if self.verbose:
            print(f"Number: {num} packet: {[hex(self.address), hex(first_byte), hex(second_byte)]}")

    def setvoltage(self, v):
        if(not (0 <= v <= self.vmax)):
            print(f"Voltage out of range [0.0v - {self.vmax}v]")
            return 0
        self.setnum(int(v/self.vmax * 2**12))