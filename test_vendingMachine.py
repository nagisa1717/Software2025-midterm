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

def test05():
    vm1 = vendingMachine.VendingMachine()
    vm1.insert_money(1000)

    buy_count = 0
    for i in range(10):
        result = vm1.buy_drinks("water")
        if i < vendingMachine.maxStock:
            buy_count += 1
            assert result == "water"
            assert vm1.payment == 1000 - vm1.drinks["water"]["price"] * buy_count
            assert vm1.drinks["water"]["stock"] == vendingMachine.maxStock - buy_count
        else:
            assert result == None
            assert vm1.payment == 1000 - vm1.drinks["water"]["price"] * buy_count
            assert vm1.drinks["water"]["stock"] == 0
'''
ユーザーがお釣りのボタンを押すと，
・ユーザーはお釣りを入手する．
・自販機内のお金が0円に戻る．
'''

def test06():
    vm1 = vendingMachine.VendingMachine()
    vm1.insert_money(200)
    result = vm1.get_change()
    assert result == 200
    assert vm1.payment == 0

    vm2 = vendingMachine.VendingMachine()
    vm2.insert_money(1000)
    vm2.buy_drinks("water")
    vm2.buy_drinks("coke")
    result = vm2.get_change()
    assert result == 1000 - (vm2.drinks["water"]["price"] + vm2.drinks["coke"]["price"])
    assert vm2.payment == 0

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
    test05()
    print("test5: OK")
    test06()
    print("test6: OK")

    print("--全てのテストをクリア--")