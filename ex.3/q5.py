class printDT:
    def __init__(self, dtype):
        self.dtype = dtype
    def pytho_data(self):
        print("The datatype is :", type(self.dtype))

a = printDT("RRR")
a.pytho_data()
b = printDT([1,2])
b.pytho_data()
c = printDT((2,3,4))
c.pytho_data()    