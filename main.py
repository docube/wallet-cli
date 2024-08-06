from views import UserViews, WalletViews, TransactionViews

def main_menu():
    active = True
    active_user = None

    paths = {
        "1": UserViews.signup,
        "2": UserViews.login,
        "3": WalletViews.deposit,
        "4": WalletViews.withdraw,
        "5": WalletViews.send,
        "6": WalletViews.view_balance,
        "7": TransactionViews.view_transactions,
        "8": TransactionViews.view_single_transaction,
        "9": UserViews.logout,
        "10": exit_program
    }

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

        if user_input == '2':
            active_user = paths[user_input](active_user)
        elif user_input == '10':
            active = False
        else:
            try:
                int(user_input)
            except ValueError:
                print('You need to enter a valid number')
                continue
            else:
                paths[user_input](active_user)

def exit_program():
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main_menu()
