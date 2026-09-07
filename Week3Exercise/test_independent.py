from bank import BankAccount
def test_deposit_independent():
    account = BankAccount(100)
    account.deposit(50)
    assert account.balance == 150

def test_withdraw_independent():
    account = BankAccount(100)
    account.withdraw(30)
    assert account.balance == 70

#good practice, each test is independent and does not rely on shared state or the order of execution
