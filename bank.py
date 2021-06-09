from datetime import datetime



class Account:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.balance=0
        self.transaction=20
        self.loan=0
        self.loan_limit=1000
        self.transactions=[]
       
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            
            transaction1={'amount':amount,'balance':self.balance,'narration':"You deposited",'time':datetime.now()}
            self.transactions.append(transaction1)
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
            transaction1={'amount':amount,'balance':self.balance,'narration':"You withdrew",'time':datetime.now()}
            self.transactions.append(transaction1)

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
            transaction1={'amount':amount,'balance':self.balance,'narration':"You borrowed",'time':datetime.now()}
            self.transactions.append(transaction1)
            return f"Hello {self.name}.You have taken a loan of {amount} and your loan balance is {self.loan}.Your current account balance is {self.balance}" 
    def repay(self,amount):
        if amount<0:
            return f"You cannot repay with amount less than 0"
        elif amount >=self.loan:
            remainder=amount-self.loan
            self.balance+=remainder
            transaction1={'amount':amount,'balance':self.balance,'narration':"You repaid",'time':datetime.now()}
            self.transactions.append(transaction1)
            return f"{amount} has been used to repay your loan,the remainder has been added to your account and balance is {self.balance}"
        else:
            self.loan-=amount
            transaction1={'amount':amount,'balance':self.balance,'narration':"You repaid",'time':datetime.now()}
            self.transactions.append(transaction1)
            return f"Your loan balance is {self.loan}"
           

    def get_statement(self):
        for items in self.transactions:
            amount=items["amount"]
            balance=items['balance']
            narration=items["narration"]
            time=items['time']
            date=time.strftime("%D")
            print(f"On {date} {narration} {amount}.Balance:{balance}")




    


             