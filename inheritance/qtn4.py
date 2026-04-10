class Complex:
    def __init__(self,r,i):
        self.r=r
        self.i=i
    
    def __add__(self, other):
        return Complex(self.r+other.r, self.i+other.i)
    
    def __mul__(self, other):
        real = self.r * other.r - self.i * other.i
        imag = self.r * other.i + self.i * other.r
        return Complex(real, imag)
    
    def __str__(self):
        return f"{self.r} +{self.i}i"

c1=Complex(1,2)
c2=Complex(4,5)
print(f"Addition: {c1+c2}")
print(f"Multiplication: {c1*c2}")