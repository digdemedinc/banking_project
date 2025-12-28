from bank_operations import deposit_money, withdraw_money

def test_deposit():
    user = {
        "balance": 100.0,
        "transactions": []
    }
    deposit_money(user, 50)
    assert user["balance"] == 150.0

def test_withdraw():
    user = {
        "balance": 100.0,
        "transactions": []
    }
    withdraw_money(user, 40)
    assert user["balance"] == 60.0

def test_overdraft():
    user = {
        "balance": 50.0,
        "transactions": []
    }
    withdraw_money(user, 100)
    assert user["balance"] == 50.0
