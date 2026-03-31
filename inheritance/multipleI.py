class Animal:
    def sound(self,name,sound):
        print(f"{name} makes {sound} sound.")

class Bird:
    def sound(self,name,sound):
        print(f"{name} makes {self.sound} sound.")

class LivingBeing(Animal,Bird):
    def sound(self, name, sound):
        print(f"{name} makes {self.sound} sound.")

l=LivingBeing()
l.sound("crow",'kawkaw')
a=Animal()
a.sound("Dog",'barks')
b=Bird()
b.sound("sparrow","chrip")