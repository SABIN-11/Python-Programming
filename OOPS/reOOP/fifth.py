# Inventory Item

class Store:

    def __init__(self, name, price, stock, balance = 0):
        self.name = name
        self.price = price
        self.stock = stock
        self.balance = balance

    def sell(self, quantity):
        if quantity > self.stock:
            print(F"NOT ENOUGH STOCK TO SELL.")
        else:
            print(F"{quantity} units of {self.name} has been sold.")
            self.stock -= quantity
            self.balance += (self.price * quantity)

    def restock(self, quantity):

        cost = self.price * quantity
        if cost > self.balance:
            print(F"Current balance is not enough for restocking {self.name}.")
        else: 
            self.stock += quantity
            self.balance -= cost
            print(F"{quantity} units of {self.name} has been restocked.")

    def set_price(self, price):
        if price <= 0:
            print("Price must be greater than zero.")
            return
        print(F"Price of one unit of {self.name} has been updated from {self.price} to {price}")
        self.price = price

    def total_value_of_stock(self):
        print(F"Current value of stock is {self.stock * self.price}")

    def current_balance(self):
        print(F"Current balance is {self.balance}")

item_1 = Store("pen", 10, 1000)
item_1.current_balance()
item_1.sell(200)    # balance - 2000
item_1.current_balance()
item_1.total_value_of_stock()   # 8000
item_1.restock(100) # balance - 1000
item_1.current_balance()
item_1.set_price(11)
item_1.sell(500)
item_1.current_balance()
item_1.total_value_of_stock()


        