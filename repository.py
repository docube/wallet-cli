import csv
import os
from models import User, Wallet, Transaction

class UserRepository:
    def __init__(self, filepath='users.csv'):
        self.filepath = filepath
        self.users = self.load_users()

    def load_users(self):
        users = {}
        if os.path.exists(self.filepath):
            with open(self.filepath, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(row['name'], row['email'], row['password'], row['user_id'])
                    users[user.user_id] = user
        return users

    def save_users(self):
        with open(self.filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name', 'email', 'password', 'user_id', 'created_at'])
            writer.writeheader()
            for user in self.users.values():
                writer.writerow(user.to_dict())

    def create_user(self, name, email, password, user_id):
        user = User(name, email, password, user_id)
        self.users[user.user_id] = user
        self.save_users()

    def authenticate_user(self, email, password):
        for user in self.users.values():
            if user.email == email and user.password == password:
                return user
        return None

    def logout(self):
        print('Logged out')
        return None

class WalletRepository:
    def __init__(self, filepath='wallets.csv'):
        self.filepath = filepath
        self.wallets = self.load_wallets()

    def load_wallets(self):
        wallets = {}
        if os.path.exists(self.filepath):
            with open(self.filepath, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    wallet = Wallet(row['wallet_id'], float(row['balance']), row['user_id'])
                    wallets[wallet.wallet_id] = wallet
        return wallets

    def save_wallets(self):
        with open(self.filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['wallet_id', 'balance', 'user_id', 'created_at'])
            writer.writeheader()
            for wallet in self.wallets.values():
                writer.writerow(wallet.to_dict())

    def create_wallet(self, wallet_id, user_id):
        wallet = Wallet(wallet_id, 0, user_id)
        self.wallets[wallet.wallet_id] = wallet
        self.save_wallets()

    def view_wallet(self, wallet_id):
        return self.wallets.get(wallet_id)

    def deposit(self, wallet_id, amount):
        wallet = self.wallets.get(wallet_id)
        if wallet:
            wallet.deposit(amount)
            self.save_wallets()
            return wallet.balance
        return None

    def withdraw(self, wallet_id, amount):
        wallet = self.wallets.get(wallet_id)
        if wallet:
            try:
                wallet.withdraw(amount)
                self.save_wallets()
                return wallet.balance
            except ValueError as e:
                print(e)
        return None

    def send(self, sender_id, receiver_id, amount):
        sender_wallet = self.wallets.get(sender_id)
        receiver_wallet = self.wallets.get(receiver_id)
        if sender_wallet and receiver_wallet:
            try:
                sender_wallet.withdraw(amount)
                receiver_wallet.deposit(amount)
                self.save_wallets()
                return True
            except ValueError as e:
                print(e)
        return False

    def view_balance(self, wallet_id):
        wallet = self.wallets.get(wallet_id)
        if wallet:
            return wallet.balance
        return None

class TransactionRepository:
    def __init__(self, filepath='transactions.csv'):
        self.filepath = filepath
        self.transactions = self.load_transactions()

    def load_transactions(self):
        transactions = []
        if os.path.exists(self.filepath):
            with open(self.filepath, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    transaction = Transaction(row['transaction_id'], row['sender'], row['receiver'], float(row['amount']))
                    transactions.append(transaction)
        return transactions

    def save_transactions(self):
        with open(self.filepath, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['transaction_id', 'sender', 'receiver', 'amount', 'created_at'])
            writer.writeheader()
            for transaction in self.transactions:
                writer.writerow(transaction.to_dict())

    def create_transaction(self, transaction_id, sender, receiver, amount):
        transaction = Transaction(transaction_id, sender, receiver, amount)
        self.transactions.append(transaction)
        self.save_transactions()

    def view_transactions(self, user_id):
        return [t for t in self.transactions if t.sender == user_id or t.receiver == user_id]

    def view_single_transaction(self, transaction_id):
        for transaction in self.transactions:
            if transaction.transaction_id == transaction_id:
                return transaction
        return None
