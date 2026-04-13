try:
    with open("1.txt","r") as f:
        print( f.read())
except FileNotFoundError as f:
    print(f)
try:
    with open("2.txt","r") as f:
        print( f.read())
except FileNotFoundError as f:
    print(f)
try:
    with open("2.txt","r") as f:
        print( f.read())
except FileNotFoundError as f:
    print(f)