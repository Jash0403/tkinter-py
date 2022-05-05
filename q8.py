numbers = [] #created an Empty List to insert the numbers
for i in range(100,401): #checking for the numbers between 100 & 400
    s = str(i) #Taking each Number as 's'
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0): #checking each digit is even or not
        numbers.append(s) #adding to the numbers(Empty List)
print( ",".join(numbers)) #printing the Numbers(List) with joining ','