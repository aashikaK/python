class Employee:
    name="himal" #this is a class attribute
    salary=300000
    age=23

e1=Employee()
print(e1.name,e1.salary)

e2=Employee()
e2.name="Binda" #this is an instance attribute
print(e2.name,e2.age)

# instance attributes take preferences over class attirbutes during assignmet or retrival