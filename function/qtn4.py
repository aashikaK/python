n=int(input("Enter the value of n: "))
print(f"The sum of n({n}) natural number is:{sum(n)}")

def sum(n):
    if(n<=0):
        return 0
    elif(n==1):
        return 1
    else:
        return n+sum(n-1)