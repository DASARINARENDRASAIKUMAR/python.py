password = input("Enter a password: ")
length = len(password) 

digit = False
upper = False
lower = False

if length < 8: 
    print("Invalid password")
else:
    for i in password:
        if i.isdigit():
            digit = True
        elif i.isupper():
            upper = True
        elif i.islower():
            lower = True

    if digit and upper and lower:
        print("Valid password")
    else:
        print("Invalid password")
