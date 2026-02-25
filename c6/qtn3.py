spam=input("Enter the comment you got to check if it is spam: ")
spam=spam.lower()
# if(spam=="make a lot of money" or spam=="buy now" or spam=="suscribe this" or spam=="click this"):
#     print("WARNING: It is spam.")
# else:
#     print("It is not spam.")


# OR

if("make a lot of money" in spam or "buy now" in spam  or "suscribe this" in spam  or "click this" in spam ):
    print("WARNING: It is spam.")
else:
    print("It is not spam.")