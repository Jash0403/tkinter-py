import random
def findRandom():
    num = random.randint(0,1)
    return num
def BinaryString(n):
    s = ""
    for i in range(n):
        x = findRandom()
        s += str(x)
    print(s)
n = int(input("Enter Number: "))
BinaryString(n)