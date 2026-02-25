n1=int(input("Enter a number: "))
n2=int(input("Enter a number: "))
n3=int(input("Enter a number: "))
n4=int(input("Enter a number: "))

if(n1>n2):
    if(n1>n3):
        if(n1>n4):
            print(n1,"is the greatest number.")

        else:
            print(n4,"is the greatest number.")
    elif(n3>n4):
        print(n3,"is the greatest number.")
    else:
        print(n4,"is the greatest number.")
elif(n2>n3):
    if(n2>n4):
        print(n2,"is the greatest number.")
    else:
        print(n4,"is the greatest number.")
else:
    if(n3>n4):
        print(n3,"is greatest number.")
    else:
        print(n4,"is the greatest number.")