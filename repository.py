import csv
import os
from models import User, Wallet, Transaction

class UserRepository:
    def __init__(self, users_file):
        self.users_file = users_file
        self.users = {}
        self.load_users()

    def load_users(self):
        if os.path.exists(self.users_file):
            with open(self.users_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.users[row[0]] = User(row[1], row[2], row[3], row[0])

    def save_users(self):
        with open(self.users_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for user_id, user in self.users.items():
                writer.writerow([user_id, user.name, user.email, user.password])

    def create_user(self, name, email, password, user_id):
        if user_id in self.users:
            return False
        self.users[user_id] = User(name, email, password, user_id)
        self.save_users()
        return True

    def authenticate_user(self, user_id, password):
        user = self.users.get(user_id)
        if user and user.password == password:
            return user
        return None

    def logout(self):
        self.user = {}
        print('Logged out')
        return {}

class WalletRepository:
    def __init__(self, wallets_file):
        self.wallets_file = wallets_file
        self.wallets = {}
        self.load_wallets()

    def load_wallets(self):
        if os.path.exists(self.wallets_file):
            with open(self.wallets_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.wallets[row[0]] = Wallet(row[0], row[1])

    def save_wallets(self):
        with open(self.wallets_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for wallet_id, wallet in self.wallets.items():
                writer.writerow([wallet_id, wallet.user_id, wallet.balance])

    def create_wallet(self, wallet_id, user_id):
        self.wallets[wallet_id] = Wallet(wallet_id, user_id)
        self.save_wallets()
        return self.wallets[wallet_id]

    def view_balance(self, wallet_id):
        wallet = self.wallets.get(wallet_id)
        if wallet:
            return wallet.balance
        return None

    def deposit(self, wallet_id, amount):
        wallet = self.wallets.get(wallet_id)
        if wallet:
            wallet.deposit(amount)
            self.save_wallets()
            return True
        return False

    def withdraw(self, wallet_id, amount):
        wallet = self.wallets.get(wallet_id)
        if wallet and wallet.withdraw(amount):
            self.save_wallets()
            return True
        return False

    def send_money(self, sender_id, receiver_id, amount):
        if self.withdraw(sender_id, amount):
            return self.deposit(receiver_id, amount)
        return False

class TransactionRepository:
    def __init__(self, transactions_file):
        self.transactions_file = transactions_file
        self.transactions = {}
        self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.transactions_file):
            with open(self.transactions_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    username = row[0]
                    txn_id = int(row[1])
                    txn_details = row[2]
                    if username not in self.transactions:
                        self.transactions[username] = []
                    self.transactions[username].append((txn_id, txn_details))

    def save_transactions(self):
        with open(self.transactions_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for username, txns in self.transactions.items():
                for txn in txns:
                    writer.writerow([username, txn[0], txn[1]])

    def create_transaction(self, sender, receiver, amount, txn_type):
        transaction_id = len(self.transactions.get(sender, [])) + 1
        transaction = Transaction(transaction_id, sender, receiver, amount, txn_type)
        if sender not in self.transactions:
            self.transactions[sender] = []
        if receiver not in self.transactions:
            self.transactions[receiver] = []
        self.transactions[sender].append((transaction_id, f"Sent ₦{amount} to {receiver}"))
        self.transactions[receiver].append((transaction_id, f"Received ₦{amount} from {sender}"))
        self.save_transactions()

    def view_transactions(self, user_id):
        return self.transactions.get(user_id, [])

    def view_single_transaction(self, user_id, transaction_id):
        transactions = self.transactions.get(user_id, [])
        for txn in transactions:
            if txn[0] == transaction_id:
                return txn
        return None
