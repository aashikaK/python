age=int(input("Enter a number: "))

if(age<0):
    raise ValueError("Age cannot be negative..")

# raise TypeError("Wrong type")
# raise ZeroDivisionError("Cannot divide")
# raise Exception("General error")