f=open('c9/poem.txt')
str=f.read()
if("twinkle" in str):
    print("There is 'twinkle' word present in the poem.txt file")
else:
     print("There is no 'twinkle' word present in the poem.txt file")
f.close()