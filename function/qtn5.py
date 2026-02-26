# ***
# **
# *

def pattern():
    n=int(input("Enter the value of n: "))
    for i in range(i,n+1):
        for j in range(j,i):
            print('*'*i, end="")
            print("")

pattern()