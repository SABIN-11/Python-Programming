# Different payment types should all have a pay() method but with completely different logic.

# Polymorphism

class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        NotImplementedError

class Credit_Card(Payment):
    def __init__(self, amount, card_no):
        super().__init__(amount)
        self.card_no = card_no

    #method overriding
    def pay(self):
        print(F"Charged ${self.amount} to card ending in {self.card_no[-1:-5:-1]}")
        
class Cash(Payment):
    def __init__(self, amount):
        super().__init__(amount)

    def pay(self):
        print(F"Paid ${self.amount} in cash.")

class Crypto(Payment):
    def __init__(self, amount, coin: int):
        super().__init__(amount)
        self.coin = coin

    def pay(self):
        print(F"Sent ${self.amount} via {self.coin} bitcoins.")


amount = 10000
paying_methods = [Credit_Card(amount, "1234576"), Cash(amount), Crypto(amount, 10)]

for payments in paying_methods:
    payments.pay()

    