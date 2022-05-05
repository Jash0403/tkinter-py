import re #re module is used for Regular Expression
passwd= input("Input your password : ") #User Input Password
a = True
while a:
    if (len(passwd)<6 or len(passwd)>16): #Checking Password is not lessthan 6 and greaterthan 16
        break
    elif not re.search("[a-z]",passwd): #searching for Samll Letters in Password
        break
    elif not re.search("[A-Z]",passwd): #searching for Captial Letters in Password
        break
    elif not re.search("[0-9]",passwd): #searching for Digits in Password
        break
    elif not re.search("[$#@]",passwd): #searching for $ or # or @ in Password
        break
    elif re.search("\s",passwd): #searching for Space in Password
        break
    else:
        print("Valid Password") #Printing if the Password Satisfied the Conditions
        a=False
        break
if a:
    print("Not a Valid Password") #Printing if the Password didn't Satisfied the Conditions