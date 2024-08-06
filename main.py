from views import UserViews, WalletViews, TransactionViews
from repository import UserRepository, WalletRepository, TransactionRepository

def main_menu():
    user_repo = UserRepository()
    wallet_repo = WalletRepository()
    transaction_repo = TransactionRepository()
    user_views = UserViews(user_repo)
    wallet_views = WalletViews(wallet_repo)
    transaction_views = TransactionViews(transaction_repo)

    active_user = None
    active = True

    while active:
        print("\nEnter the corresponding numbers to perform an action.")
        user_input = input("1. Create Account\n"
                           "2. Sign-in to your Account\n"
                           "3. Deposit Money \n"
                           "4. Withdraw Money \n"
                           "5. Send Money \n"
                           "6. Check Balance \n"
                           "7. My Transactions \n"
                           "8. View single transaction\n"
                           "9. Sign out \n"
                           "10. Exit App \n"
                           )
        if user_input == '1':
            active_user = user_views.signup()
        elif user_input == '2':
            active_user = user_views.login()
        elif user_input == '9':
            active_user = user_views.logout()
        elif user_input == '10':
            active = False
        else:
            if not active_user:
                print("Please login or signup first.")
                continue
            if user_input == '3':
                wallet_views.deposit(active_user.user_id)
            elif user_input == '4':
                wallet_views.withdraw(active_user.user_id)
            elif user_input == '5':
                wallet_views.send(active_user.user_id)
            elif user_input == '6':
                wallet_views.view_balance(active_user.user_id)
            elif user_input == '7':
                transaction_views.view_transactions(active_user.user_id)
            elif user_input == '8':
                transaction_views.view_single_transaction()
            else:
                print('You need to enter a valid number')

if __name__ == "__main__":
    main_menu()
