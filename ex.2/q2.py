def areRotations(wd1,wd2):
    size1 = len(wd1)
    size2 = len(wd2)
    temp = ''
    if size1 != size2:
        return 0
    temp = wd1 + wd1
    if (temp.count(wd2) > 0):
        return 1
    else:
        return 0

wd1 = input("Enter 1st Word: ")
wd2 = input("Enter 2nd Word: ")
if areRotations(wd1,wd2):
    print("TRUE")
else:
    print("FALSE")