f=open('c9/poem.txt')
str=f.read()
if("twinkle" in str):
    print("There is 'twinkle' in the poem.txt file")

f.close()