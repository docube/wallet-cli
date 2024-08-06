from views import UserViews, WalletViews, TransactionViews

# URL patterns mapping
url_patterns = {
    "1": UserViews.signup,
    "2": UserViews.login,
    "3": WalletViews.deposit,
    "4": WalletViews.withdraw,
    "5": WalletViews.send,
    "6": WalletViews.view_balance,
    "7": TransactionViews.view_transactions,
    "8": TransactionViews.view_single_transaction,
    "9": UserViews.logout,
    "10": "exit_program"  # This will be handled directly in the main_menu function
}
