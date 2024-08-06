import psycopg2
from psycopg2 import sql

def get_db_connection():
    connection = psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='your_db_host',
        port='your_db_port'
    )
    return connection

def create_tables():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        password VARCHAR
