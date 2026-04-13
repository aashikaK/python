# # finally block ALWAYS executes no mater what:error, no error

# try:
#     n=int(input("Enter a number: "))

# except ValueError as v:
#     print(v)

# finally:
#     print("Hello!")

# Why use finally?

# 👉 For cleanup work, like:

# closing files 📁
# closing database connections
# releasing resources 

try:
    file = open("test.txt")
    data = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")
    file.close()

