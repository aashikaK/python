# ***
# **
# *

def pattern():
    n=int(input("Enter the value of n: "))
    for i in range(1,n+1):
        # for j in range(i,n+1):
        #     print('*', end="")
        # print("")
        print("*"*(n-i+1))

pattern()