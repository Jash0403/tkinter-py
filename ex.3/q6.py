class Banks_SRMIST:
    indian, hdfc, cub = 0, 0, 0

    def getbalance(self):
        return 0


class CUB(Banks_SRMIST):
    def __init__(self):
        self.cub = 15000

    def getbalance(self):
        return self.cub


class HDFC(Banks_SRMIST):
    def __init__(self):
        self.hdfc = 30000

    def getbalance(self):
        return self.hdfc


class Indian_Bank(Banks_SRMIST):
    def __init__(self):
        self.indian = 40000

    def getbalance(self):
        return self.indian


hd = HDFC()
ind = Indian_Bank()
cu = CUB()
print(ind.getbalance())
print(cu.getbalance())
print(hd.getbalance())