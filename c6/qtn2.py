marks1=int(input("Enter marks of Science: "))
marks2=int(input("Enter marks of Computer: "))
marks3=int(input("Enter marks of Maths: "))

# check for total percentages asuming total marks is 100 each
tPercent=((marks1+marks2+marks3)/300)*100

# m1Per=(marks1/100)*100
# m2Per=(marks2/100)*100
# m3Per=(marks3/100)*100

if(tPercent>=40 and marks1>=33 and marks2>=33 and marks3>=33):
   print(f"You have passed. Total Percentage -> {tPercent:.2f}%")
else:
    print(f"You have failed.Total Percentage-> ,{tPercent:.2f}%")