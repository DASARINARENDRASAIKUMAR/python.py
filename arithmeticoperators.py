a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=input("Enter the operation:")
if(c=='+'):
    print(a+b)
elif(c=='-'):
    print(a-b)
elif(c=='*'):
    print(a*b)
elif(c=='/'):
    print(a/b)
elif(c=='%'):
    print(a%b)
else:
    print("Invaild operation")
