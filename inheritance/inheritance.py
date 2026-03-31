class Employee:
    emp_no=2
    def info(self,company):
        print(f"Employee of company: {company}")
class Prog(Employee):
    def info(self):
        print(f"Employee:{self.emp_no} of company: {self.company}")

e=Employee()
e.info("Tech")
p=Prog()
p.info()
