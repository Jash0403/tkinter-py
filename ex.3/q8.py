import math
class Triangle:

    def __init__(self):
        self.sides = [3,4,5]

    def area(self):
        s = sum(self.sides)/2
        area = math.sqrt((s*(s - self.sides[0])*(s - self.sides[1])*(s - self.sides[2])))
        print("area of traingle",area)
    def peri(self):
        print("perimeter of traingle",self.sides[0] + self.sides[1] + self.sides[2])
tri = Triangle()
tri.area()
tri.peri()