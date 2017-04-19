class Account:
    count = 0
    def __init__(self, accId, holderName, balance):
        self.accId = accId
        self.holderName = holderName
        self.balance = balance
        Account.count+=1
        
    def withdraw(self, amt):
        self.balance = self.balance - amt
        
    def deposit(self, amt):
        self.balance = self.balance + amt
        
class SavingAcc(Account):
    
    def __init__(self, accId, holderName, balance, minBal):      
        super().__init__(accId, holderName, balance)  
        self.minBal = minBal
        
sv1 = SavingAcc(101, 'Ankur', 10000, 1000)
sv2 = SavingAcc(101, 'Ankur', 10000, 1000)

sv1.withdraw(2000)
print(getattr(sv1, 'balance'))
print('Count: ' +str(Account.count))

            