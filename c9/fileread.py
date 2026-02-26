
f=open("c9/file.txt")
# data=f.read()
# print(data)

lines= f.readlines()
print(lines,type(lines)) #readlines reads all line and returns a list (each line represent an element of list)


line1=f.readline() #reads only single line
print(line1,type(line1))

line2=f.readline()
print(line2,type(line2))

line3=f.readline()
print(line3,type(line3))

line4=f.readline()
print(line4,type(line4))

line5=f.readline()
print(line5,type(line5)) #there is no line so it gives empty string we can also use while loop like

line=f.readline()
while(f.readline()!=""):
    print(line,type(line))
    line=f.readline()

f.close()

