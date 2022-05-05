def comb(x):
    print("\nPossible Combinations of the given 3 Digits:")
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i != j and j != k and i != k):
                    print(x[i],x[j],x[k])

str= input("Enter List: ")
lst= str.split(",")
comb(lst)