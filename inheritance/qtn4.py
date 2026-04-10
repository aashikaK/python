class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    
    def __add__(self, other):
        return Complex(self.r+other.r, self.i+other.r)

c1=Complex(1,2)
c2=Complex(4,5)
print(c1+c2)