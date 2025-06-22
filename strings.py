a="this is assigning value to an string"
print(a)
# use different quote if u want to use itt while printing
print("It's alright")
print("It is called 'MELON'.")
print('It is called "MELON".')

# multiline strings
b="""I am
going
to the 
zoo"""
c='''I am
very happy.'''
print(b)
print(c)

d="Hi what are you doing?"
print(d[2])

e="banana"
for x in e:
    print (x)

print(len(e)) #to calculate the lengh

#chheckingg if certain word or phrae s present or not
txt="I am free todaay"
print("free" in txt)
#or
if "am" in txt:
    print("'am' is present in the text")

print("free" not in txt)

if "are" not in txt:
    print(' "are" is not present in the text')