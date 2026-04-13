# else runs only when try block has NO error

try:
    x = int(input("Enter number: "))
    print(10 / x)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

else:
    print("Everything worked fine")