a=int(input("Enter your age: "))

# if statement no:1
if(a%2==0):
    print("Your age is even.")
#end of if statement no:1

# if statement no:2
if(a>18):
    print("You are an adult.")

elif(a<0):
    print("Age can't be negative.Enter correct age.")
    int(input("Enter correct age: "))

elif(a==0):
    print("You entered an ivalid age..")
    int(input("Enter correct age: "))

else:
    print("You are not an adult.")

 #end of if statement no:2

print("The end.")