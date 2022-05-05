l = []
n = int(input("Enter no. of elements "))

for i in range(0, n):
    ele = int(input())
    l.append(ele)


def test_distinct(data):
    if len(l) == len(set(l)):
        return True
    else:
        return False


print(test_distinct(l))