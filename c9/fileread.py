
f=open("c9/file.txt")
# data=f.read()
# print(data)

lines= f.readlines()
print(lines,type(lines)) #readlines reads all line and returns a list (each line represent an element of list)
f.close()

