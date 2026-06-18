class employee:
    name="mahindra"
    salary=123456
    def show2(self):
     print(f"he name of the employee is {self.name} and the salary of empmis {self.salary}")

class progrmer1(employee):
    salary=123456
    name="input(type)"
    def show(self): 
      print(f"he name of the employee is {self.name} and the salary of empmis {self.salary}")

    def show_lang(self):
        print(f"he name of the employee is {self.name} and the salary of empmis {self.salary}")

class progrmer(progrmer1):
    def __init__(self):
        super().__init__()
    def show1(self): 
     salary=123456
     name="input(type)"

    
     print(f"he name of the employee is {self.name} and the salary of empmis {self.salary}")

    def show_lang1(self):
        print(f"he name of the employee is {self.name} and the salary of empmis {self.salary}")

a=employee()
b=progrmer()

b.show()
print(b.show_lang1(),b.show1())