class Attribute:
    a=78 #class attribute

o=Attribute()
o.a=0 #object attribute
print(o.a)

# o.a=0-> it doesnot change class attribute 
print(Attribute.a)