class Student:
    def set_name(self, name):
        self.name = name

    def show(self):
        print("My name is", self.name)

    def __init__(self,name): #dunder method automatically called
        # self.name=name no need this bcz we r noy using object but local variable and You are NOT storing anything inside the object
        print(f"This is constructor called each time a object is created.Name={name}")

s1 = Student("Aashika")
s2 = Student("Ram")
s1.set_name("Aashika")
# Student.set_name(s1, "Aashika") python does this internally
s2.set_name("Ram")
#Student.set_name(s2, "Ram") python does this internally
s1.show()
s2.show()

#python does Student.show(s1/s2)