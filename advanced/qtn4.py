try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    div=a/b
    print("Division of two numbers is: ",div)
except ZeroDivisionError:
    print("Infinite number.")