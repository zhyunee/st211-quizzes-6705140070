from bank import BankAccount

def test_deposit_increases_balance():
    account = BankAccount(100)
    new_balance = account.deposit(50)
    assert new_balance == 150
    
def test_withdraw_decreases_balance():
    account = BankAccount(100)
    new_balance = account.withdraw(30)
    assert new_balance == 70
    
def test_everything_at_once():
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    account.deposit(10)
    assert account.balance == 130
