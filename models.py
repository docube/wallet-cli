from datetime import datetime

class User:
    def __init__(self, name, email, password, user_id):
        self.name = name
        self.email = email
        self.password = password
        self.user_id = user_id
        self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "user_id": self.user_id,
            "created_at": self.created_at
        }

class Wallet:
    def __init__(self, wallet_id, balance, user_id):
        self.wallet_id = wallet_id
        self.balance = balance
        self.user_id = user_id
        self.created_at = datetime.now()
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")
    
    def to_dict(self):
        return {
            "wallet_id": self.wallet_id,
            "balance": self.balance,
            "user_id": self.user_id,
            "created_at": self.created_at
        }

class Transaction:
    def __init__(self, transaction_id, sender, receiver, amount):
        self.transaction_id = transaction_id
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.created_at = datetime.now()
    
    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "created_at": self.created_at
        }
