#自販機のテストを順に行う
import vendingMachine
import random

def test01(vm):
    assert vm.payment == 0
    for stock in vm.drinks.values():
        assert stock == vendingMachine.maxStock

def test02(vm):
    before_payment = vm.payment
    vm.insert_money(100)
    assert vm.payment == before_payment + 100

    for i in range(10):
        before_payment = vm.payment
        money = random.randint(1,10000)
        vm.insert_money(money)
        assert vm.payment == before_payment + money

if __name__ == "__main__":
    print("-------テスト開始-------")
    vm1 = vendingMachine.VendingMachine()

    test01(vm1)
    print("test1: OK")
    test02(vm1)
    print("test2: OK")

    print("--全てのテストをクリア--")