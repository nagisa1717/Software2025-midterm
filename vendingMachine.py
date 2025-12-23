#プログラム本文．自販機のシミュレーションを作成する．
maxStock = 5

class VendingMachine():
    def __init__(self):
        self.payment = 0
        self.drinks = {
            "water": {"stock": maxStock, "price":100},
            "tea": {"stock": maxStock, "price":130},
            "coke": {"stock": maxStock, "price":150}
        }
    def insert_money(self, money):
        self.payment += money
    def buy_drinks(self, drink):
        if self.payment >= self.drinks[drink]["price"] and self.drinks[drink]["stock"] > 0:
            self.payment -= self.drinks[drink]["price"]
            self.drinks[drink]["stock"] -= 1
            return drink
        else:
            return None
