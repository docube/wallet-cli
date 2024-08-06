from models import User, Wallet, Transaction
import csv
import os

# In-memory storage
users = {}
wallets = {}
transactions = {}

# User repository
class UserRepository:
    @staticmethod
    def create_user(name, email, password):
        user = User(name, email, password)
        users[user.user_id] = user
        WalletRepository.create_wallet(user.user_id)
        return user

    @staticmethod
    def authenticate_user(email, password):
        for user in users.values():
            if user.email == email and user.password == password:
                return user
        return None

    @staticmethod
    def logout():
        print("Logged out")
        return {}

# Wallet repository
class WalletRepository:
    @staticmethod
    def create_wallet(user_id):
        wallet = Wallet(user_id)
        wallets[user_id] = wallet
        return wallet

    @staticmethod
    def deposit(user_id, amount):
        wallets[user_id].deposit(amount)

    @staticmethod
    def withdraw(user_id, amount):
        wallets[user_id].withdraw(amount)

    @staticmethod
    def send(sender_id, receiver_id, amount):
        wallets[sender_id].withdraw(amount)
        wallets[receiver_id].deposit(amount)
        TransactionRepository.create_transaction(sender_id, receiver_id, amount)

    @staticmethod
    def view_balance(user_id):
        return wallets[user_id].balance

# Transaction repository
class TransactionRepository:
    @staticmethod
    def create_transaction(sender_id, receiver_id, amount):
        transaction = Transaction(sender_id, receiver_id, amount)
        transactions.setdefault(sender_id, []).append(transaction)
        transactions.setdefault(receiver_id, []).append(transaction)

    @staticmethod
    def view_transactions(user_id):
        return transactions.get(user_id, [])

    @staticmethod
    def view_single_transaction(user_id, transaction_id):
        for txn in transactions.get(user_id, []):
            if txn.transaction_id == transaction_id:
                return txn
        return None
