class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addi(self):
     print(f"a+b",self.a+self.b)  

    def multi(self):
     print(f"a+b",self.a*self.b) 

    def sub(self):
     print(f"a+b",self.a-self.b) 
    def div(self):
     print(f"a+b",self.a/self.b) 
    def mod(self):
     print(f"a+b",self.a%self.b) 
c=calculator(1234,123)
c.addi()
c.sub()
c.multi()
c.mod()
c.div()    