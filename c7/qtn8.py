'''
***
* *
*** for n=3
'''
n= int(input("Enter the value of n: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        star="*"*n
        print(star, end="")
        print("")
    else:
        space=(n-2)*" "
        print("*",space,"*",end="")
        print("")