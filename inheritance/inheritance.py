class Employee:
    emp_no=2
    def info(self,company):
        self.company=company
        print(f"Employee of company: {self.company}")
class Prog(Employee):
    def info(self):
        print(f"Employee:{self.emp_no} of company: {self.company}")

e=Employee()
e.info("Tech")
p=Prog()
p.company="Tech"
p.info()
