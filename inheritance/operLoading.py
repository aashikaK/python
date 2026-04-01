class Number:
    def __init__(self,n):
        self.n=n
    
    def __add__(self, other):
        return self.n+other.n
n1=Number(5)
n2=Number(3)
print(n1+n2)
