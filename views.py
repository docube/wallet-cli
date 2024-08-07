from repository import UserRepository, WalletRepository, TransactionRepository

user_repo = UserRepository('users.csv')
wallet_repo = WalletRepository('wallets.csv')
txn_repo = TransactionRepository('transactions.csv')

def signup():
    print("Sign Up")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if user_repo.create_user(name, email, password, username):
        wallet_repo.create_wallet(username, username)
        print("Sign up successful! Logging you in...")
        login(username, password)
    else:
        print("Username already exists. Please try a different one.")

def login(username=None, password=None):
    print("Log In")
    if username is None:
        username = input("Enter your username: ")
    if password is None:
        password = input("Enter your password: ")

    user = user_repo.authenticate_user(username, password)
    if user:
        print("Login successful!")
        dashboard(username)
    else:
        print("Incorrect username or password. Please try again.")

def dashboard(username):
    print(f"Welcome to your wallet, {username}!")
    while True:
        print("\nPlease select an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Send money")
        print("4. View balance")
        print("5. View transactions")
        print("6. View single transaction")
        print("7. Logout")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")
        if choice == '1':
            deposit_money(username)
        elif choice == '2':
            withdraw_money(username)
        elif choice == '3':
            send_money(username)
        elif choice == '4':
            view_balance(username)
        elif choice == '5':
            view_transactions(username)
        elif choice == '6':
            view_single_transaction(username)
        elif choice == '7':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def deposit_money(username):
    amount = float(input("Enter the amount to deposit: ₦"))
    wallet_repo.deposit(username, amount)
    txn_repo.create_transaction(username, username, amount, "Deposit")
    print(f"Deposited ₦{amount} successfully.")

def withdraw_money(username):
    amount = float(input("Enter the amount to withdraw: ₦"))
    if wallet_repo.withdraw(username, amount):
        txn_repo.create_transaction(username, username, -amount, "Withdrawal")
        print(f"Withdrew ₦{amount} successfully.")
    else:
        print("Insufficient balance.")

def send_money(username):
    recipient = input("Enter the recipient's username: ")
    if recipient not in user_repo.users:
        print("Recipient not found.")
        return

    amount = float(input("Enter the amount to send: ₦"))
    if wallet_repo.send_money(username, recipient, amount):
        txn_repo.create_transaction(username, recipient, amount, "Send")
        print(f"Sent ₦{amount} to {recipient} successfully.")
    else:
        print("Transaction failed due to insufficient balance or other issues.")

def view_balance(username):
    balance = wallet_repo.view_balance(username)
    print(f"Your current balance is: ₦{balance}")

def view_transactions(username):
    transactions = txn_repo.view_transactions(username)
    if not transactions:
        print("No transactions found.")
        return
    print("Your transactions:")
    for txn in transactions:
        print(f"{txn[0]}. {txn[1]}")

def view_single_transaction(username):
    txn_id = int(input("Enter the transaction ID to view details: "))
    txn = txn_repo.view_single_transaction(username, txn_id)
    if txn:
        print(f"Transaction {txn_id}: {txn[1]}")
    else:
        print("Transaction ID not found.")
