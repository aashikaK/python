def i_to_c(i):
    cm=i*2.54
    return cm

i=int(input("Enter the value of inch to convert into cm: "))
cm=i_to_c(i)
print(f'inch {i} converted to cm gives {cm}cm')