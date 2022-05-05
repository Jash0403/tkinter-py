import math
x1,y1=int(input("Enter 1st Point x-coordinate Number: ")),int(input("Enter 1st Point y-coordinate Number: "))
x2,y2=int(input("Enter 2nd Point x-coordinate Number: ")),int(input("Enter 2nd Point y-coordinate Number: "))
dist=math.sqrt((x2-x1)*2+(y2-y1)*2)
print(dist)