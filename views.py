from repository import UserRepository, WalletRepository, TransactionRepository

class UserViews:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def signup(self):
        print("Sign Up")
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        password = input("Enter a password: ")
        user_id = str(len(self.user_repo.users) + 1)
        self.user_repo.create_user(name, email, password, user_id)
        print("Sign up successful! Logging you in...")
        return self.user_repo.authenticate_user(email, password)

    def login(self):
        print("Log In")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        user = self.user_repo.authenticate_user(email, password)
        if user:
            print("Login successful!")
            return user
        else:
            print("Incorrect email or password. Please try again.")
            return None

    def logout(self):
        return self.user_repo.logout()

class WalletViews:
    def __init__(self, wallet_repo):
        self.wallet_repo = wallet_repo

    def view_wallet(self, user_id):
        wallet = self.wallet_repo.view_wallet(user_id)
        if wallet:
            print(f"Wallet ID: {wallet.wallet_id}, Balance: {wallet.balance}")

    def view_balance(self, user_id):
        balance = self.wallet_repo.view_balance(user_id)
        if balance is not None:
            print(f"Your current balance is: ₦{balance}")
        else:
            print("Wallet not found.")

    def send(self, sender_id):
        recipient_id = input("Enter the recipient's wallet ID: ")
        amount = float(input("Enter the amount to send: ₦"))
        if self.wallet_repo.send(sender_id, recipient_id, amount):
            print(f"Sent ₦{amount} to {recipient_id} successfully.")
        else:
            print("Failed to send money.")

    def deposit(self, wallet_id):
        amount = float(input("Enter the amount to deposit: ₦"))
        balance = self.wallet_repo.deposit(wallet_id, amount)
        if balance is not None:
            print(f"Deposited ₦{amount}. New balance: ₦{balance}")

    def withdraw(self, wallet_id):
        amount = float(input("Enter the amount to withdraw: ₦"))
        balance = self.wallet_repo.withdraw(wallet_id, amount)
        if balance is not None:
            print(f"Withdrew ₦{amount}. New balance: ₦{balance}")

class TransactionViews:
    def __init__(self, transaction_repo):
        self.transaction_repo = transaction_repo

    def view_transactions(self, user_id):
        transactions = self.transaction_repo.view_transactions(user_id)
        if transactions:
            for txn in transactions:
                print(f"{txn.transaction_id}: {txn.amount} - {txn.created_at}")
        else:
            print("No transactions found.")

    def view_single_transaction(self):
        txn_id = input("Enter the transaction ID: ")
        transaction = self.transaction_repo.view_single_transaction(txn_id)
        if transaction:
            print(f"Transaction ID: {transaction.transaction_id}, Amount: {transaction.amount}, Time: {transaction.created_at}")
        else:
            print("Transaction not found.")
