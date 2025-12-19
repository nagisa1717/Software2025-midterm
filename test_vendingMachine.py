#自販機のテストを順に行う
import vendingMachine

def test01(vm):
    '''
    初期状態では
    ・自販機内のお金は0円である．
    ・初期状態では飲み物の在庫は充填されている．(満タンの本数を5本とする．)
    '''
    assert vm.payment == 0
    for stock in vm.drinks.values():
        assert stock == vendingMachine.maxStock

if __name__ == "__main__":
    print("-------テスト開始-------")
    vm1 = vendingMachine.VendingMachine()

    test01(vm1)
    print("test1: OK")

    print("--全てのテストをクリア--")