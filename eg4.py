# write  python program to prin the contents of a directory using the os odule...
# ...Search online for the function which does that
import os

# Specify the directory path
# directory_path = input("Enter the path of the directory: ")
directory_path= '/'

try:
    # List all files and directories
    contents = os.listdir(directory_path)
    print(f"\nContents of '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("Error: The specified directory does not exist.")
except PermissionError:
    print("Error: You do not have permission to access this directory.")

