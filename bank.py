
# class Account:
#     def __init__(self,accNumber,type,owner,balance):
#         self.accNumber=accNumber
#         self.type=type
#         self.owner=owner
#         self.balance=balance
#     def description(self):
#         return f"Account with {self.accNumber} owned by {self.owner} is a {self.type} account"   
#     def initialAmmount(self):
#        return 10000+self.balance
#     def statement(self):
#         return f"Your balance is {self.balance}"


class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction=20
        self.loan=0
        self.loan_limit=1000
       
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            return f"Hello {self.name},you have deposited {amount}.Your new balance is {self.balance}"
        else:
            return "Please deposit a valid amount" 
    def withdraw(self,amount):
        newbalance=amount+self.transaction
        
        if amount<=0:
            return "I cannot withdraw zero or less"
        elif newbalance>self.balance:
            return "I cannot withdraw if the balance is less than the amount plus transaction fee"
        else:
            self.balance-=newbalance
            return f"Hello {self.name},you have withrawn{amount}.Your new balance is {self.balance}"
    def loanB(self,amount):
        if amount<0:
            return "You cannot get a loan"
        elif self.loan>0:
            return "You cannot get a loan if you have an outstanding loan balance"
        elif amount>self.loan_limit:
            return "You cannot if the amount is greater than loan limit"    
        else:
            loan_fee=0.05*amount
            self.loan=amount+loan_fee
            self.balance+=amount
            return f"Hello {self.name}.You have taken a loan of {amount} and your loan balance is {self.loan}.Your current account balance is {self.balance}"       





    


             