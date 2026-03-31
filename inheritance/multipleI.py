class Animal:
    def sound(self,name,sounds):
        print(f"{name} makes {sounds} sound.")

class Bird:
    def sound(self,name,sound):
        print(f"{name} makes {self.sounds} sound.")

class LivingBeing(Animal,Bird):
    def sound(self, name, sound):
        print(f"{name} makes {self.sounds} sound.")

l=LivingBeing()
l.sound("crow",'kawkaw')
a=Animal()
a.sound("Dog",'barks')
b=Bird()
b.sound("sparrow","chrip")