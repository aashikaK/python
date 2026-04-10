class Employee:
    salary=60000
    increment=20
    @property
    def salaryAfterIncrement(self):
        return (self.salary+(self.salary*(self.increment/100)))

e=Employee()
print(f"Salary after increment: {e.salaryAfterIncrement}")