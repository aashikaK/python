f=open("c9/file.txt")
print(f.read())
f.close()

# we can do same using with statement
with open('c9/file.txt') as f:
    print(f.readlines())

    # Now using with  dont have to explicitely close the file

 
