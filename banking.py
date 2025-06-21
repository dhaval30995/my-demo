class bankacount:
    def __init__(self,name,balance = 0):
        self.name = name
        self.balance  = balance
    
    def credit(self,amount):
        self.balance += amount
        return f"hi {self.name} {amount} is credited in your account your balance is {self.balance}"
    
    def debit(self,amount):
        self.balance -= amount
        return f"hi {self.name} {amount} is debited in your account your balance is {self.balance}"
    
    def checkbalance(self):
        return f'your available balacnce is {self.balance}'
    
acc1 = bankacount('dhaval',0)
cr = int(input('please enter amount for credit :- '))
print(acc1.credit(cr))
db = int(input('please enter amount for debit:- '))
print(acc1.debit(db))
print(acc1.checkbalance())