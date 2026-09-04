# modeling a bank account

class bank_account:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(F"{amount} has been deposited to the account named {self.name}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(F"Insufficient Funds.")
        else:
            print(F"{amount} has been withdrawn from the account named {self.name}")
            self.balance -= amount

    def get_balance(self):
        print(F"Current bank balance in the account named {self.name} is {self.balance}")


def create_account(name) -> bank_account:
    print(F"New bank account named {name} has been created.")
    return bank_account(name)

acc_name = input("Enter the name of the account: ")
inst_1 = create_account(acc_name)
inst_1.get_balance()
inst_1.deposit(10000)
inst_1.withdraw(5000)
inst_1.get_balance()
