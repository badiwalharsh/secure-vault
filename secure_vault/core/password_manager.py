import sqlite3
import os

DB_PATH = os.path.join("data", "passwords.db")

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_password(category, username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO passwords (category, username, password) VALUES (?, ?, ?)",
                   (category, username, password))
    conn.commit()
    conn.close()

def get_passwords():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT category, username, password FROM passwords")
    rows = cursor.fetchall()
    conn.close()
    return rows
