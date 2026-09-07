from bank import BankAccount

shared_account = BankAccount(100)

def test_a_deposit():
    shared_account.deposit(50)
    assert shared_account.balance == 150
    
def test_b_withdraw():
    shared_account.withdraw(30)
    assert shared_account.balance == 120

  #bad test, sharing a object between tests, tests are dependent on each other, and order of execution matters
