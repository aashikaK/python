
class Person:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def show_info(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Status: I have studied only inheritance in OOP")


s1 = Student("Aashika", "Computer Science")
s1.show_info()