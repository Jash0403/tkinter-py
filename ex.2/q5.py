x=tuple(map(int,input("Enter 1st Tuple: ").split(',')))
y=tuple(map(int,input("Enter 2nd Tuple: ").split(',')))
z=tuple(map(int,input("Enter 3rd Tuple: ").split(',')))

print("\nx: ",x)
print("y: ",y)
print("z: ",z)
print("\nElement-wise sum of the Tuples:")
result = tuple(map(sum, zip(x, y, z)))
print(result)