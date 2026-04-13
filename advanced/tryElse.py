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

# Why use else?

# To separate:

# risky code → inside try
# safe code (only if success) → inside else