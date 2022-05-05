phn=input()
missing=[]
for i in  range(10):
    if not str(i) in phn:
        missing.append(i)
print(missing)