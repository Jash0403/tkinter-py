str= input("Enter List: ")
lst_input= str.split(",")
lst = []
count = 0
for item in lst_input:
    if item not in lst:
        count += 1
        lst.append(item)
print("No of unique items in the given List are ", count)