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
            interest_earned = self.balance * self.int_rate
            self.balance += interest_earned

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def make_deposit(self, account, amount):
        for acc in self.accounts:
            if acc.account_number == account:
                acc.deposit(amount)
                break

    def make_withdraw(self, account, amount):
        for acc in self.accounts:
            if acc.account_number == account:
                acc.withdraw(amount)
                break

    def display_user_balance(self, account):
        for acc in self.accounts:
            if acc.account_number == account:
                acc.display_account_info()
                break

    def transer_money(self, amount, other_user, from_account, to_account):
        for acc in self.accounts:
            if acc.account_number == from_account:
                acc.withdraw(amount)
                break

        for acc in other_user.accounts:
            if acc.account_number == to_account:
                acc.deposit(amount)
                break




my_account = BankAccount()
account_2 = BankAccount(.1, 23300938)
my_account.deposit(1000)
my_account.deposit(443)
my_account.deposit(1200)
my_account.withdraw(500)
print(my_account)
my_account.display_account_info()
account_2.deposit(4324)
account_2.deposit(3223)
account_2.withdraw(5000)
account_2.withdraw(3322)
account_2.withdraw(522)
account_2.withdraw(900)
account_2.display_account_info()

