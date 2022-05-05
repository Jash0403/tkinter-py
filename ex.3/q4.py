class Rectangle:
    length=0
    breadth=0
    def area(self):
        print(self.length*self.breadth)
    def __init__(self,*args):
        if len(args)==0:
            self.length=0
            self.breadth=0
        elif len(args)==1:
            self.length = args[0]
            self.breadth = args[0]
        elif len(args)==2:
            self.length=args[0]
            self.breadth=args[1]

obj=Rectangle()
obj.area()
obj1=Rectangle(5)
obj1.area()
obj2=Rectangle(5,6)
obj2.area()