def test(n,m):
    if n==m==5 or n+m==5 or abs(n-m)==5:
        return True
    else:
        return False
a,b=int(input("Enter 1st Number: ")),int(input("Enter 2nd Number: "))
print(test(a,b))