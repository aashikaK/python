x="Awesome"
def fun1():
    print("python is",x) #comma prints with space
fun1()

a="wow"
def fun2():
    a="haha"
    print("I am "+a) #a is now local in this block it will not be used after the block finishes
fun2()
print("I am",a)


# using 'global' keyword

def fun3():
    global b
    b= "wow"
fun3()
print("Aashika is "+b)

c="stupid"
def fun4():
    global c #now it overwrites above c
    c="mad"
fun4()
print("Why are you",c+"?")