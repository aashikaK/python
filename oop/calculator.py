class Calculator:
    
    def __init__(self,num):
        self.num=num

    def square(self):
        print("Square= ",self.num*self.num)
    def cube(self):
        n=self.num
        print("Cube= ",n*n*n)
    def sqRt(self):
        n=self.num
        print("Square Root= ",n**(1/2):.2f) #n^1/2

c= Calculator(64)
c.square()
c.cube()
c.sqRt()