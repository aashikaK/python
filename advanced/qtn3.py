try:
    n=int(input("Enter a number: "))
except ValueError as v:
    print(v)

else:
    list=[1,2,3,4,5,6,7,8,9,10]
    multiplication=[]
    for i in list:
        multiplication.append(n*i)
    print(multiplication)