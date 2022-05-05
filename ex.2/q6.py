t = list(tuple(map(str,input("Enter Tuple: ").split())) for r in range(int(input('Enter No of Rows : '))))
print("List of Tuples Given is ",t)
t= [x for x in t if x]
print("List of Tuples without Empty-Tuples: ",t)