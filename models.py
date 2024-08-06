from datetime import datetime

class User:
    def __init__(self, name, email, password, user_id):
        self.name = name
        self.email = email
        self.password = password
        self.user_id = user_id
        self.created_at = datetime.now()

class Wallet:
    def __init__(self, wallet_id, user_id):
        self.wallet_id = wallet_id
        self.balance = 0.0
        self.user_id = user_id
        self.created_at = datetime.now()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

class Transaction:
    def __init__(self, transaction_id, sender, receiver, amount):
        self.transaction_id = transaction_id
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.created_at = datetime.now()
