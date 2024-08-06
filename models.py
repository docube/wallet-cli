from datetime import datetime
import uuid

# User class
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.user_id = str(uuid.uuid4())
        self.created_at = datetime.now()

# Wallet class
class Wallet:
    def __init__(self, user_id):
        self.wallet_id = str(uuid.uuid4())
        self.balance = 0.0
        self.user_id = user_id
        self.created_at = datetime.now()

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

# Transaction class
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.transaction_id = str(uuid.uuid4())
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = datetime.now()
