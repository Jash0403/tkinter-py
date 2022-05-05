def sum(a,b):
    sum=a+b
    if sum in range(105,201):
        return 200
    else:
        return sum
n,m=int(input("Enter First Number : ")),int(input("Enter Second Number : "))
print(sum(n,m))