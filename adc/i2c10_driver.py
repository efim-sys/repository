import smbus

class MCP3021:
    def __init__(self, vmax, verbose = False):
        self.bus = smbus.SMBus(1)

        self.address = 0x4D
        self.verbose = verbose
        self.vmax = vmax
    
    def deinit(self):
        self.bus.close()

    def getnum(self):
        data = self.bus.read_word_data(self.address, 0)

        ld = data >> 8
        ud = data & 0xff

        num = (ud << 6) | (ld >> 2)

        if(self.verbose):
            print(f'num = {num}')

        return num

    def getvoltage(self):
        return self.getnum()/(2**10) * self.vmax * (3.3/2.1)