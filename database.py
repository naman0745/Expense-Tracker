import mysql.connector
from datetime import datetime

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin1234",
        database="tracker"
    )

def insert_transaction(trans_type, category, amount):
    db = connect_db()
    cursor = db.cursor()
    date = datetime.now().strftime('%Y-%m-%d')
    query = "INSERT INTO transactions (type, category, amount, date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (trans_type, category, amount, date))
    db.commit()
    db.close()

def fetch_transactions():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    results = cursor.fetchall()
    db.close()
    return results

def calculate_balance():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'gain'")
    total_gain = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type = 'expense'")
    total_expense = cursor.fetchone()[0] or 0

    db.close()
    return total_gain - total_expense
