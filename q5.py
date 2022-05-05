m,n=int(input("Enter Rows ")),int(input("Enter Columns "))
arr= [[0 for j in range(n)] for i in range(m)]
for i in range(m):
    for j in range(n):
        arr[i][j]= i*j
print(arr)