# SECURE ATM - Encapsulation

class ATM:
    def __init__(self, pin, balance = 0):
        self.__pin = pin    # private by name mangling
        self.balance = balance

    def authenticate(self, pin):    # checking if entered pin is correct or not
        return self.__pin == pin
    
    def deposit(self, pin, amount):
        authentication = self.authenticate(pin)
        if authentication:
            self.balance += amount
            print(F"{amount} has been deposited in the account.")
        else:
            print(F"Invalid PIN.")

    def withdraw(self, pin, amount):
        authentication = self.authenticate(pin)
        if authentication:
            if amount > self.balance:
                print(F"Insufficient Funds!")
            else:
                print(F"{amount} has been withdrawn from the account.")
                self.balance -= amount
        else:
            print(F"Invalid PIN.")

    def check_balance(self, pin):
        authentication = self.authenticate(pin)
        if authentication:
            print(F"Current balance is {self.balance}")
        else:
            print("Invalid PIN.")    


pin = 3456
atm_1 = ATM(3456)
atm_1.check_balance(pin)
atm_1.deposit(pin, 50000)
atm_1.check_balance(pin)
atm_1.withdraw(pin, 30000)
atm_1.check_balance(pin)