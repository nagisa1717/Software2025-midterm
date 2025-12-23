#プログラム本文．自販機のシミュレーションを作成する．
maxStock = 5

class VendingMachine():
    def __init__(self):
        self.payment = 0
        self.drinks = {
            "water": {"stock": maxStock, "price":100},
            "tea": {"stock": maxStock, "price":130},
            "coke": {"stock": maxStock, "price":150},
            "coffee": {"stock": maxStock, "price":180}
        }
    def insert_money(self, money):
        self.payment += money
    def can_buy(self, drink_name):
        return self.payment >= self.drinks[drink_name]["price"] and self.drinks[drink_name]["stock"] > 0
    def buy(self, drink_name):
        if drink_name not in self.drinks:
            raise ValueError("Unknown drink")
        if self.can_buy(drink_name):
            self.payment -= self.drinks[drink_name]["price"]
            self.drinks[drink_name]["stock"] -= 1
            return drink_name
        else:
            return None
    def get_change(self):
        change = self.payment
        self.payment = 0
        return change
