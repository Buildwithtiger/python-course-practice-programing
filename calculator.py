class calculator:
    def __init__(self,a):
        self.a=a
    def cube(self):
       
        print(f"the cubbe is {self.a*self.a*self.a} of")
    def squre(self):
        
        print(f"the cubbe is {self.a*self.a} of")

    def root(self):
        
        print(f"the cubbe is {self.a**1/2} of")
c=calculator(3)
c.cube()
c.squre()
c.root()
