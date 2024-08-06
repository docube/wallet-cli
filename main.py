from urls import url_patterns

def main_menu():
    active = True
    active_user = None

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
            active_user = url_patterns[user_input](active_user)
        elif user_input == '3' or '4' or '5' or '6' or '7' or '8' or '9':
            print("Please Sign/up or Login first")
        elif user_input == '10':
            active = False
        else:
            try:
                int(user_input)
            except ValueError:
                print('You need to enter a valid number')
                continue
            else:
                url_patterns[user_input](active_user)

def exit_program():
    print("Exiting the program.")
    exit()

if __name__ == "__main__":
    main_menu()
