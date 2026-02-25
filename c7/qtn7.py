'''
  *
 ***
*****
'''
n= int(input("Enter the value of n: "))
for i in range(1,n+1):
    space=n-i
    star=((2*i)-1)
    print(space *" "+ star*"*")
    # print("\n")
    