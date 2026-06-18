class twodvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"the vector is {self.i} + {self.j} ")
class tthreedvector(twodvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"the vector is {self.i} + {self.j} +{self.k}")  
a=twodvector(1,4)
a.show()
b=tthreedvector(1,4,9)
b.show()