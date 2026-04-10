class Employee:
    salary=60000
    increment=20
    @property
    def salaryAfterIncrement(self):
        return (self.salary+(self.salary*(self.increment/100)))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment=((salary/self.salary)-1)*100

e=Employee()
new_salary = e.salaryAfterIncrement
e.salaryAfterIncrement=new_salary
print(f"Increment:{round(e.increment,0)}")