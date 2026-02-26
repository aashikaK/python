# ***
# **
# *

# def pattern():
#     n=int(input("Enter the value of n: "))
#     for i in range(1,n+1):
#         # for j in range(i,n+1):
#         #     print('*', end="")
#         # print("") OR
#         print("*"*(n-i+1))

def pattern(n):
    if(n==0):
        print("")
    print("*"*n)
    pattern(n-1)


n=int(input("Enter the value of n: "))
pattern(n)