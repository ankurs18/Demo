import logging
from fileinput import filename

logging.basicConfig(filename='account.log', level=logging.INFO) #1st parameter is d file name andlogging levels are:debug info warn error

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
        logging.debug('DEBUG: deposit method')
        logging.info('INFO: deposit method')
        logging.warn('WARN: deposit method')
        self.balance = self.balance + amt
        
class SavingAcc(Account):
    
    def __init__(self, accId, holderName, balance, minBal):      
        super().__init__(accId, holderName, balance)  
        self.minBal = minBal
        
sv1 = SavingAcc(101, 'Ankur', 10000, 1000)
sv2 = SavingAcc(101, 'Ankur', 10000, 1000)
sv2.deposit(2000)
sv1.withdraw(2000)
print(getattr(sv1, 'balance'))
print('Count: ' +str(Account.count))

            