s=input("Enter ")
letters=digits=0
for a in s:
    if a.isdigit():
        digits=digits+1
    elif a.isalpha():
        letters=letters+1
    else:
        pass
print("Letters ",letters)
print("Digits ",digits)