class Employee:
    a=2
    @classmethod
    def show(cls):
        print(f"The value of class attribute is: {cls.a}")  #since this is class method it wont ...
        #... show 45(object attribute) but class attribute bcz we used class method
e=Employee()
e.a=45
e.show()