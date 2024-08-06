from repository import UserRepository, WalletRepository, TransactionRepository

class UserViews:
    @staticmethod
    def signup(_):
        print("Sign Up")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = UserRepository.create_user(name, email, password)
        print("Sign up successful! Logging you in...")
        return user

    @staticmethod
    def login(_):
        print("Log In")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = UserRepository.authenticate_user(email, password)
        if user:
            print("Login successful!")
            return user
        else:
            print("Incorrect email or password. Please try again.")
            return None

    @staticmethod
    def logout(user):
        return UserRepository.logout()

class WalletViews:
    @staticmethod
    def deposit(user):
        amount = float(input("Enter the amount to deposit: ₦"))
        WalletRepository.deposit(user.user_id, amount)
        print(f"Deposited ₦{amount} successfully.")

    @staticmethod
    def withdraw(user):
        amount = float(input("Enter the amount to withdraw: ₦"))
        try:
            WalletRepository.withdraw(user.user_id, amount)
            print(f"Withdrew ₦{amount} successfully.")
        except ValueError as e:
            print(e)

    @staticmethod
    def send(user):
        receiver_email = input("Enter the recipient's email: ")
        amount = float(input("Enter the amount to send: ₦"))
        receiver = None
        for usr in UserRepository.users.values():
            if usr.email == receiver_email:
                receiver = usr
                break
        if receiver:
            try:
                WalletRepository.send(user.user_id, receiver.user_id, amount)
                print(f"Sent ₦{amount} to {receiver.email} successfully.")
            except ValueError as e:
                print(e)
        else:
            print("Recipient not found.")

    @staticmethod
    def view_balance(user):
        balance = WalletRepository.view_balance(user.user_id)
        print(f"Your current balance is: ₦{balance}")

class TransactionViews:
    @staticmethod
    def view_transactions(user):
        txns = TransactionRepository.view_transactions(user.user_id)
        if not txns:
            print("No transactions found.")
            return
        for txn in txns:
            print(f"{txn.transaction_id}. {txn.sender} sent {txn.amount} to {txn.receiver} on {txn.timestamp}")

    @staticmethod
    def view_single_transaction(user):
        txn_id = input("Enter the transaction ID: ")
        txn = TransactionRepository.view_single_transaction(user.user_id, txn_id)
        if txn:
            print(f"{txn.transaction_id}. {txn.sender} sent {txn.amount} to {txn.receiver} on {txn.timestamp}")
        else:
            print("Transaction ID not found.")
