mjr_lst=[]
n=int(input("Enter Number Lists in the Matrix: "))
for i in range(0,n):
    x = list(tuple(map(int,input("Enter Tuple: ").split(','))) for r in range(int(input("Enter No of Tuples in List : "))))
    mjr_lst.append(x)

print("\nThe Matrix is ",mjr_lst)
temp = [ele for sub in mjr_lst for ele in sub]
res = list(zip(*temp))
print("\nThe converted tuple list : " + str(res))