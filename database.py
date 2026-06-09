import sqlite3

DB_NAME = "sharemate.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        assigned_to TEXT NOT NULL,
        due_date TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS shopping_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT NOT NULL,
        added_by TEXT NOT NULL,
        status TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settlements (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        content TEXT NOT NULL,
        debtor TEXT NOT NULL,
        creditor TEXT NOT NULL,
        amount REAL NOT NULL,
        status TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def get_chores():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM chores ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def add_chore(title, assigned_to, due_date):
    conn = get_connection()
    conn.execute(
        "INSERT INTO chores (title, assigned_to, due_date, status) VALUES (?, ?, ?, ?)",
        (title, assigned_to, due_date, "진행 전")
    )
    conn.commit()
    conn.close()


def update_chore_status(chore_id, status):
    conn = get_connection()
    conn.execute(
        "UPDATE chores SET status = ? WHERE id = ?",
        (status, chore_id)
    )
    conn.commit()
    conn.close()


def get_shopping_items():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM shopping_items ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def add_shopping_item(item_name, added_by):
    conn = get_connection()
    conn.execute(
        "INSERT INTO shopping_items (item_name, added_by, status) VALUES (?, ?, ?)",
        (item_name, added_by, "구매 필요")
    )
    conn.commit()
    conn.close()


def update_shopping_status(item_id, status):
    conn = get_connection()
    conn.execute(
        "UPDATE shopping_items SET status = ? WHERE id = ?",
        (status, item_id)
    )
    conn.commit()
    conn.close()


def get_settlements():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM settlements ORDER BY id DESC").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def add_settlement(content, debtor, creditor, amount):
    conn = get_connection()
    conn.execute(
        "INSERT INTO settlements (content, debtor, creditor, amount, status) VALUES (?, ?, ?, ?, ?)",
        (content, debtor, creditor, amount, "대기")
    )
    conn.commit()
    conn.close()


def update_settlement_status(settlement_id, status):
    conn = get_connection()
    conn.execute(
        "UPDATE settlements SET status = ? WHERE id = ?",
        (status, settlement_id)
    )
    conn.commit()
    conn.close()

def delete_chore(chore_id):
    conn = get_connection()
    conn.execute(
        "DELETE FROM chores WHERE id = ?",
        (chore_id,)
    )
    conn.commit()
    conn.close()

def delete_shopping_item(item_id):
    conn = get_connection()
    conn.execute(
        "DELETE FROM shopping_items WHERE id = ?",
        (item_id,)
    )
    conn.commit()
    conn.close()

def delete_settlement(settlement_id):
    conn = get_connection()
    conn.execute(
        "DELETE FROM settlements WHERE id = ?",
        (settlement_id,)
    )
    conn.commit()
    conn.close()