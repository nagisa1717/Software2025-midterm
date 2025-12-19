#プログラム本文．自販機のシミュレーションを作成する．
maxStock = 5

class VendingMachine():
    def __init__(self):
        self.payment = 0
        self.drinks = {
            "water": maxStock,
            "tea": maxStock,
            "coke": maxStock
        }
