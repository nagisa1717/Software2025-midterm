#自販機のテストを順に行う
import vendingMachine
import random
MaxStock = vendingMachine.maxStock

def test_init(): #項目1のテスト
    vm = vendingMachine.VendingMachine()
    assert vm.payment == 0
    for drink in vm.drinks.values():
        assert drink["stock"] == MaxStock

def test_insert_money(): #項目2のテスト
    vm = vendingMachine.VendingMachine()
    before_payment = vm.payment
    vm.insert_money(100)
    assert vm.payment == before_payment + 100

    for i in range(10):
        before_payment = vm.payment
        money = random.randint(1,10000)
        vm.insert_money(money)
        assert vm.payment == before_payment + money

def test_can_buy(): #項目3のテスト
    # water
    vm1 = vendingMachine.VendingMachine()
    vm1.insert_money(100)
    result = vm1.buy("water")
    assert result == "water"
    assert vm1.payment == 100 - vm1.drinks["water"]["price"]
    assert vm1.drinks["water"]["stock"] == MaxStock - 1

    # tea
    vm2 = vendingMachine.VendingMachine()
    vm2.insert_money(150)
    result = vm2.buy("tea")
    assert result == "tea"
    assert vm2.payment == 150 - vm2.drinks["tea"]["price"]
    assert vm2.drinks["tea"]["stock"] == MaxStock - 1

    # coke
    vm3 = vendingMachine.VendingMachine()
    vm3.insert_money(200)
    result = vm3.buy("coke")
    assert result == "coke"
    assert vm3.payment == 200 - vm3.drinks["coke"]["price"]
    assert vm3.drinks["coke"]["stock"] == MaxStock - 1

def test_cannot_buy(): #項目4のテスト
    # water
    vm1 = vendingMachine.VendingMachine()
    vm1.insert_money(50)
    result = vm1.buy("water")
    assert result == None
    assert vm1.payment == 50
    assert vm1.drinks["water"]["stock"] == MaxStock

    # tea
    vm2 = vendingMachine.VendingMachine()
    vm2.insert_money(0)
    result = vm2.buy("tea")
    assert result == None
    assert vm2.payment == 0
    assert vm2.drinks["tea"]["stock"] == MaxStock

    # coke
    vm3 = vendingMachine.VendingMachine()
    vm3.insert_money(100)
    result = vm3.buy("coke")
    assert result == None
    assert vm3.payment == 100
    assert vm3.drinks["coke"]["stock"] == MaxStock

def test_lack_change(): #項目5のテスト
    vm1 = vendingMachine.VendingMachine()
    vm1.insert_money(1000)

    buy_count = 0
    for i in range(10):
        result = vm1.buy("water")
        if i < MaxStock:
            buy_count += 1
            assert result == "water"
            assert vm1.payment == 1000 - vm1.drinks["water"]["price"] * buy_count
            assert vm1.drinks["water"]["stock"] == MaxStock - buy_count
        else:
            assert result == None
            assert vm1.payment == 1000 - vm1.drinks["water"]["price"] * buy_count
            assert vm1.drinks["water"]["stock"] == 0

def test_get_change(): #項目6のテスト
    vm1 = vendingMachine.VendingMachine()
    vm1.insert_money(200)
    result = vm1.get_change()
    assert result == 200
    assert vm1.payment == 0

    vm2 = vendingMachine.VendingMachine()
    vm2.insert_money(1000)
    vm2.buy("water")
    vm2.buy("coke")
    result = vm2.get_change()
    assert result == 1000 - (vm2.drinks["water"]["price"] + vm2.drinks["coke"]["price"])
    assert vm2.payment == 0

if __name__ == "__main__":
    print("-------テスト開始-------")
    
    test_init()
    print("test1: OK")
    test_insert_money()
    print("test2: OK")
    test_can_buy()
    print("test3: OK")
    test_cannot_buy()
    print("test4: OK")
    test_lack_change()
    print("test5: OK")
    test_get_change()
    print("test6: OK")

    print("--全てのテストをクリア--")