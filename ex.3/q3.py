class Dept:
    def __init__(self, name="SCO"):
        self.deptname =name
    def pri(self):
        print("Dpt :", self.deptname)

dept = Dept()
dept.pri()
dept1 = Dept("SMO")
dept1.pri()