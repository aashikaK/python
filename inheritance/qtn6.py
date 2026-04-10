class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    
    def __add__(self, other):
        result= Vector(self.x+other.x, self.y+other.y, self.z+other.z)
        return result
    
    def __mul__(self, other):
        result= self.x*other.x +self.y*other.y+self.z*other.z
        return result
    def __str__(self):
        return f"Vector({self.x}i + {self.y}j + {self.z}k)"

v1=Vector(1,2,3)
v2=Vector(2,4,5)
v3=Vector(5,6,2)

print("Sum: ",v1+v2)
print("Sum: ",v1+v3)
print("Sum: ",v2+v3)
print(f"Multiplication: {v1*v2}")
print(f"Multiplication: {v1*v3}")
print(f"Multiplication: {v2*v3}")