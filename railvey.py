from random import randint;

class Railvey:
    def __init__(tiger,tno):
     tiger.tno=tno

    def book(tiger,frm,to):
      print(f"ticket is bboked in tran no {tiger.tno} from {frm} to {to}")
    
    def getstatus(tiger):
      print(f"the train is runnring sucess fully {tiger.tno}")
    
    def getfare(tiger,frm,to):
     print(f"ticket is fare  in tran no {tiger.tno} from {frm} to {to} is {randint( 456,5555)}")

r=Railvey(45)
r.book("rampoor","palistan")
r.getfare("himalay","goa")