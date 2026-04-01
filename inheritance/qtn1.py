class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"The value of i and j are: {self.i} and {self.j}")

class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"The value of i,j and k are: {self.i}, {self.j}and {self.k}")

a=TwoDVector(1,2)
b=ThreeDVector(3,4,5)    
a.show()
b.show()