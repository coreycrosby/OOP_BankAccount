class BankAccount:

    interest_rate = 0.04
    accounts = []

    def __init__(self, name, balance = 0): 
        self.name = name
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self.balance

    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
        return self.balance

    @classmethod
    def create(cls, name):
        cls.accounts.append(name)

    @classmethod
    def total_funds(cls):
        total_balance = 0
        for account in cls.accounts:
            total_balance += account.balance
        return total_balance

    @classmethod
    def interest_time(cls):
        for account in cls.accounts:
            account.balance += account.balance * cls.interest_rate
        print(f'{account.name} - {account.balance}')


acc1 = BankAccount("chequing")
acc2 = BankAccount("savings")

BankAccount.create(acc1)
BankAccount.create(acc2)

print(acc2.balance)
print(BankAccount.total_funds())

acc2.deposit(200)


print(acc1.balance)
print(acc2.balance)

print(BankAccount.total_funds())

BankAccount.interest_time()

print(acc1.balance)
print(acc2.balance)
print(BankAccount.total_funds())

acc2.withdraw(100)

print(acc2.balance)

print(BankAccount.total_funds())