import psycopg2

def create_connection():
    return psycopg2.connect(
        database="your_database_name",
        user="your_database_user",
        password="your_database_password",
        host="your_database_host",
        port="your_database_port"
    )

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id VARCHAR PRIMARY KEY,
        name VARCHAR NOT NULL,
        email VARCHAR NOT NULL,
        password VARCHAR NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS wallets (
        wallet_id VARCHAR PRIMARY KEY,
        user_id VARCHAR REFERENCES users(user_id),
        balance FLOAT DEFAULT 0.0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id SERIAL PRIMARY KEY,
        sender VARCHAR REFERENCES wallets(wallet_id),
        receiver VARCHAR REFERENCES wallets(wallet_id),
        amount FLOAT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_user(user):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO users (user_id, name, email, password)
    VALUES (%s, %s, %s, %s)
    """, (user.user_id, user.name, user.email, user.password))
    conn.commit()
    cursor.close()
    conn.close()

def insert_wallet(wallet):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO wallets (wallet_id, user_id, balance)
    VALUES (%s, %s, %s)
    """, (wallet.wallet_id, wallet.user_id, wallet.balance))
    conn.commit()
    cursor.close()
    conn.close()

def insert_transaction(transaction):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO transactions (sender, receiver, amount)
    VALUES (%s, %s, %s)
    """, (transaction.sender, transaction.receiver, transaction.amount))
    conn.commit()
    cursor.close()
    conn.close()
