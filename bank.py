
class Bank:
    def __init__(self,accNumber,type,owner,balance):
        self.accNumber=accNumber
        self.type=type
        self.owner=owner
        self.balance=balance
    def description(self):
        return f"Account with {self.accNumber} owned by {self.owner} is a {self.type} account"   
    def initialAmmount(self):
       return 10000+self.balance
    def statement(self):
        return f"Your balance is {self.balance}"


             