
def convert(celc):
    f=(celc*9/5)+32
    print(f"The value of {celc} degree celcius in farhenheit is {round(f,2)}")

c=int(input("Enter the temperature in degree celcius: "))
convert(c)