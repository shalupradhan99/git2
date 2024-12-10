  class Bankaccount:
     def __init__(self,account_holder,balance=0):
         self.account_holder=account_holder
         self.balance=balance

     def deposit(self,amount):
         self.balance+=amount
         print(f"deposited${amount},new balance:${self.balance}")
     def withdraw(self,amount):
      if amount>self.balance:
          print(f"insufficient fund!current balance:${self.balance}")
      else:
          self.balance-=amount
          print(f"withdrew${amount}.new balance:${self.balance}")





  account=Bankaccount( account_holder="shalu",balance=1000000)
  account.deposit(50000)
  account.withdraw(30000)
  account.withdraw(20000)




