# backend/db.py
import os
import sqlite3
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "../ids.db")


def init_db():
    """Create the SQLite database and table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            src_ip TEXT,
            dst_ip TEXT,
            type TEXT,
            details TEXT
        )
    """)
    conn.commit()
    conn.close()


def insert_incident(src_ip, dst_ip, attack_type, details):
    """Insert a new security incident into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO incidents (timestamp, src_ip, dst_ip, type, details)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, src_ip, dst_ip, attack_type, details))
    conn.commit()
    conn.close()


def get_recent_incidents(limit=10):
    """Fetch the latest incidents from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM incidents ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows
