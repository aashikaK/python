class Animal:
    def __init__(self,sound):
        self.sound=sound
    def makes(self):
        print(f"This animal {self.sound}")
class Dog(Animal):
    def __init__(self, sound):
        super().__init__(sound)
d=Dog("barks")
d.makes()