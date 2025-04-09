class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw=100
        self.max_withdraw=1000
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
     
    def withdraw(self,amount):
         if amount<self.min_withdraw:
             print( f'fokir{self.min_withdraw}')
         elif amount >self.max_withdraw:
             print( f'bank fokir hoiye jabe{self.max_withdraw}')
         else:
             self.balance-=amount
             print( f'here is your money {amount}')
brac=Bank(15000)
brac.withdraw(250)