def great(a,b,c):
    greatest=a
    if(b>greatest and b>c):
        greatest=b
    elif(c>greatest and c>b):
        greatest=c
    return greatest

greatest=great(4,5,3)
print("The greatest number among the three numbers is: ",greatest)