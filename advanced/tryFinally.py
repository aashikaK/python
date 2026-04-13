# finally block ALWAYS executes no mater what:error, no error

try:
    n=int(input("Enter a number: "))

except ValueError as v:
    print(v)

finally:
    print("Hello!")
