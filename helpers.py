import csv
import os
from repository import users, wallets, transactions

def load_data():
    if os.path.exists('users.csv'):
        with open('users.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                users[row[0]] = row[1:]

    if os.path.exists('wallets.csv'):
        with open('wallets.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                wallets[row[0]] = float(row[1])

    if os.path.exists('transactions.csv'):
        with open('transactions.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                username = row[0]
                txn_id = int(row[1])
                txn_details = row[2]
                if username not in transactions:
                    transactions[username] = []
                transactions[username].append((txn_id, txn_details))

def save_data():
    with open('users.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for user_id, user in users.items():
            writer.writerow([user_id] + user)

    with open('wallets.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for user_id, balance in wallets.items():
            writer.writerow([user_id, balance])

    with open('transactions.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for user_id, txns in transactions.items():
            for txn in txns:
                writer.writerow([user_id, txn[0], txn[1]])

# Load data on startup
load_data()
