from views import signup, login, deposit_money, withdraw_money, send_money, view_balance, view_transactions, view_single_transaction

commands = {
    1: signup,
    2: login,
    3: deposit_money,
    4: withdraw_money,
    5: send_money,
    6: view_balance,
    7: view_transactions,
    8: view_single_transaction,
}

paths = {1: signup, 2: login}
