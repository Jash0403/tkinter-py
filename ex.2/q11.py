def even(x):
    for num in x:
        if num % 2 == 0:
            print(num)

lst=list(map(int,input("Enter List: ").split(',')))
even(lst)