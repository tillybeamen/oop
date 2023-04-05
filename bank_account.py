class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            print(f"You deposited: ${amount}.")
            self.balance += amount
        else:
            print("Please make a deposit")


    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            print(f"Thank you for withdrawing: ${amount}")
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee!")
            self.balance -= 5

    
    def display_account_info(self):
        print(f"You have a balance of: ${self.balance}")
        print(f"Your interest rate is: {self.int_rate * 100}%")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            interest_earned = self.balance *self.int_rate
            self.balance += interest_earned

my_account = BankAccount()
account_2 = BankAccount(.1, 23300938)
my_account.deposit(1000)
my_account.deposit(443)
my_account.deposit(1200)
my_account.withdraw(500)
print(my_account)
my_account.display_account_info()
