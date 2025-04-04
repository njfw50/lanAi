import sqlite3
import os

DB_PATH = "lanAi.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

def insert_knowledge(source, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO knowledge (source, content) VALUES (?, ?)", (source, content))
    conn.commit()
    conn.close()

def get_all_knowledge():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT content FROM knowledge")
    results = cursor.fetchall()
    conn.close()
    return "\n".join([r[0] for r in results])
