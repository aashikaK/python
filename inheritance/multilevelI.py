class Living:
    @staticmethod
    def does():
        print("Living Beings breathe.")

class Animal(Living):
    def sound(self,name,sound):
        print(f"{name} makes {sound} sound.")

class Dog(Animal):
    pass

d=Dog()
d.sound('Dog','barking')
a=Animal()
a.does()
