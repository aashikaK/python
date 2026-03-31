class Animal:
    def sound(self,name,sounds):
        print(f"{name} makes {sounds} sound.")

class Bird:
    @staticmethod
    def fly():
        print('Birds fly.')
    # def sound(self,name,sound):
    #     print(f"{name} makes {self.sound} sound.")

class LivingBeing(Animal,Bird):
    pass
    # def sound(self, name, sound):
    #     print(f"{name} makes {self.sound} sound.")

l=LivingBeing()
l.sound("Crow",'kawkaw')
l.fly()
# a=Animal()
# a.sound("Dog",'barks')
# b=Bird()
# b.sound("sparrow","chrip")