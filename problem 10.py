class BankAccount:
    def __init__(self, balance=0):
        self.balance  = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        self.balance += self.balance * self.interest_rate

# Usage example
account = SavingsAccount(balance=1000, interest_rate=0.05)
account.deposit(500)
account.withdraw(200)
account.add_interest()
print("Final balance:", account.balance)
