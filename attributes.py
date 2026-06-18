class emp:
    name="surry"
    lang="martahi"
    def getinfo(self):
        print(f"my name is{self.name} and my language is {self.lang}")
    @staticmethod
    def greet():
        print("good morning")
e=emp()
e.getinfo()
e.greet()