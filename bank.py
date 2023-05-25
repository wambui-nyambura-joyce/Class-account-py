# class Account:
#     bank = "Equity"
#     def __init__(self,account_name,account_number,branch):
#         self.account_name = account_name
#         self.account_number = account_number
#         self.branch = branch
#     def deposit(self):
#          return(f"Joy deposited her salary savings in her {self.account_name} bank account.")
#     def withraw(self):
#          return(f"Joy accessed her {self.account_name} through her {self.account_number} to withdraw her medical fee.")
#     def display_balance(self):
#          return(f"Joy accessed her {self.account_name} in the {self.branch} to check her account balance.") 
     
class Bank:
        bank_name="Equity"
        def __init__(self,account_name,account_number,balance,deposits,withdrawals,loan_balance):
             self.account_name=account_name
             self.account_number=account_number
             self.balance=balance
             self.deposits=deposits
             self.withdrawals=withdrawals
             self.loan_balance=0
        def deposit(self,amount):
            self.balance+=amount
            self.deposits.append({
                 "amount":amount,
                 "narration":"deposit"
            })
            return(f"I now have {self.balance} in my account")
        def withdraw(self,amount):
            if self.balance <= amount:
              return(f"You have insufficient amount")
            else:
             self.balance-=amount
             self.withdrawals.append({
                   "amount":amount ,
                   "narration":"withdrawals"
              })
             return (f"You have {self.balance} remaining")
        def current_amount(self):
         return(f"Your current balance stands at {self.balance}")
        def print_statement(self):
           statement=""
           transactions=self.deposits + self.withdrawals
           for transaction in transactions:
             amount= transaction["amount"]
           narration=transaction["narration"]
           statement+= f"{narration}:{amount}\n"
           return statement
        def borrow_loan(self,amount):
            if self.loan_balance==0 and amount>100 and len(self.deposits) >= 10:
              total_deposits=sum(transaction["amount"]for transaction in self.deposits)
              borrowed_loan =total_deposits/3
              if amount<=borrowed_loan:
                   self.loan_balance+=amount
                   print ("Loan successfuly borrowed ")
              else:
                   print ("Loan borrowed exceeds limit")
            else :
              print("Loan does not meet requirements")
        def repay_loan(self,amount):
         if amount<=self.loan_balance:
              self.loan_balance-=amount
         else:
              overpayment=amount-self.loan_balance
              self.loan_balance=0
              self.balance+=overpayment
        def transfer(self, amount, transfer_account):
         if amount <= self.balance:
            self.balance -= amount
            transfer_account.deposit(amount)
            print(f"{amount} transferred to account number {transfer_account.account_number}.")
         else:
            print("Insufficient funds!")
Esther=Bank(account_name="Esther",account_number="54678A",balance=50000,deposits=[],withdrawals=[],loan_balance=0)
Peter=Bank(account_name="Peter",account_number="54656A",balance=100000,deposits=[],withdrawals=[],loan_balance=0)
print(Esther.deposit(10000))
print(Esther.withdraw(20000))
print(Esther.current_amount())
print(Esther.deposits)
print(Esther.withdrawals)
print(Esther.print_statement())
print(Esther.deposit(500))
print(Esther.deposit(200))
print(Esther.deposit(350))
print(Esther.deposit(560))
print(Esther.deposit(20000))
print(Esther.deposit(150))
print(Esther.deposit(1200))
print(Esther.deposit(12000))
print(Esther.deposit(700))
print(Esther.deposits)
print(Esther.borrow_loan(20000))
print(Esther.loan_balance)
print(Peter.deposit(30000))
print(Peter.withdraw(50000))
print(Peter.current_amount())
print(Peter.deposits)
print(Peter.withdrawals)
print(Peter.print_statement())
# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount