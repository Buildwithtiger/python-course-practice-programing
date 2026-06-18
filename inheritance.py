class employee:
    name="mahindra"
    salary=123456
    def show1(self):
     print(f"he name of the employee is {self.name} and the salary of empmis {self.salary}")

class progrmer(employee):
    salary=123456
    name="input(type)"
    def show(self): 
      print(f"he name of the employee is {self.name} and the salary of empmis {self.salary}")

    def show_lang(self):
        print(f"he name of the employee is {self.name} and the salary of empmis {self.salary}")

a=employee()
b=progrmer()

b.show()
print(b.show(),b.show_lang(),b.show1())