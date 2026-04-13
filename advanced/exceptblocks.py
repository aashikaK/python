try:
    a = int(input("Enter number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print(result)

except ValueError:
    print("Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero!")

except Exception:
    print("Some other error occurred")