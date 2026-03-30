class Student:
    def set_name(self, name):
        self.name = name

    def show(self):
        print("My name is", self.name)
    
    @staticmethod
    # doesnot need self, called using class name, no need obj creation
    def print():
        print('This is static method belonging to class')

s1 = Student()
s2 = Student()
s1.set_name("Aashika")
# Student.set_name(s1, "Aashika") python does this internally
s2.set_name("Ram")
#Student.set_name(s2, "Ram") python does this internally
s1.show()
s2.show()

Student.print()
#python does Student.show(s1/s2)