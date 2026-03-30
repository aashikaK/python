class Programmer:
    company="Microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p= Programmer("Aashika",12000000,230)
print(p.name,p.company,p.salary,p.pin)