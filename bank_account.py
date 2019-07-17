class BankAccount:
    interest_rate = 0.01
    accounts = []
    

    def __init__(self):
        self.balance = 0

    def deposit(self, dep_amount):
        self.balance += dep_amount

    def withdraw(self, with_amount):
        if self.balance > with_amount:
            self.balance -= with_amount
        else:
            print("You do not have enough funds")

    @classmethod
    def create(cls):
        new = BankAccount()
        cls.accounts.append(new)
        return new

    @classmethod
    def total_funds(cls): 
        return sum(account.balance for account in cls.accounts)

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += account.balance * cls.interest_rate
    
my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0