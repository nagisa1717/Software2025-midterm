#自販機のテストを順に行う
import vendingMachine
import random

def test01():
    vm = vendingMachine.VendingMachine()
    assert vm.payment == 0
    for drink in vm.drinks.values():
        assert drink["stock"] == vendingMachine.maxStock

def test02():
    vm = vendingMachine.VendingMachine()
    before_payment = vm.payment
    vm.insert_money(100)
    assert vm.payment == before_payment + 100

    for i in range(10):
        before_payment = vm.payment
        money = random.randint(1,10000)
        vm.insert_money(money)
        assert vm.payment == before_payment + money

def test03():
    # water
    vm1 = vendingMachine.VendingMachine()
    vm1.insert_money(100)
    result = vm1.buy_drinks("water")
    assert result == "water"
    assert vm1.payment == 100 - vm1.drinks["water"]["price"]
    assert vm1.drinks["water"]["stock"] == vendingMachine.maxStock - 1

    # tea
    vm2 = vendingMachine.VendingMachine()
    vm2.insert_money(150)
    result = vm2.buy_drinks("tea")
    assert result == "tea"
    assert vm2.payment == 150 - vm2.drinks["tea"]["price"]
    assert vm2.drinks["tea"]["stock"] == vendingMachine.maxStock - 1

    # coke
    vm3 = vendingMachine.VendingMachine()
    vm3.insert_money(200)
    result = vm3.buy_drinks("coke")
    assert result == "coke"
    assert vm3.payment == 200 - vm3.drinks["coke"]["price"]
    assert vm3.drinks["coke"]["stock"] == vendingMachine.maxStock - 1

'''
ユーザーが飲み物のボタンを押すと，「飲み物の金額 > 自販機内のお金」の場合，
・ユーザーは何も入手しない．
・飲み物の在庫は変化しない．
・自販機内のお金は変化しない．
'''
def test04():
    # water
    vm1 = vendingMachine.VendingMachine()
    vm1.insert_money(50)
    result = vm1.buy_drinks("water")
    assert result == None
    assert vm1.payment == 50
    assert vm1.drinks["water"]["stock"] == vendingMachine.maxStock

    # tea
    vm2 = vendingMachine.VendingMachine()
    vm2.insert_money(0)
    result = vm2.buy_drinks("tea")
    assert result == None
    assert vm2.payment == 0
    assert vm2.drinks["tea"]["stock"] == vendingMachine.maxStock

    # coke
    vm3 = vendingMachine.VendingMachine()
    vm3.insert_money(100)
    result = vm3.buy_drinks("coke")
    assert result == None
    assert vm3.payment == 100
    assert vm3.drinks["coke"]["stock"] == vendingMachine.maxStock

if __name__ == "__main__":
    print("-------テスト開始-------")
    
    test01()
    print("test1: OK")
    test02()
    print("test2: OK")
    test03()
    print("test3: OK")
    test04()
    print("test4: OK")

    print("--全てのテストをクリア--")