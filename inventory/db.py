# inventory/db.py
'''db file represents the database connection and operations.
This file is responsible for managing the connection to the database,
executing queries, and handling transactions.'''

import sqlite3
from pathlib import Path
from inventory.models import InventoryItem

DB_PATH = Path("data/inventory.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                quantity REAL NOT NULL,
                unit TEXT,
                vendor TEXT,
                price REAL,
                par_level REAL
            )
        ''')
        conn.commit()

def insert_item(item: InventoryItem):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO inventory (name, category, quantity, unit, vendor, price, par_level)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            item.name,
            item.category, 
            item.quantity, 
            item.unit, 
            item.vendor or "Unknown", 
            item.price, 
            get_par_level(item.name)
            ))
        conn.commit()

def get_par_level(name: str):
    from inventory.processor import PAR_LEVELS
    return PAR_LEVELS.get(name)

def fetch_low_stock() -> list[InventoryItem]:
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT name, category, quantity, unit, vendor, price, par_level
        FROM inventory
        WHERE par_level IS NOT NULL AND quantity < par_level
        ''')
        rows = cursor.fetchall()
        
    # Convert rows to InventoryItem objects
    return [
        InventoryItem(
            name=row[0],
            category=row[1],
            quantity=row[2],
            unit=row[3],
            vendor=row[4],
            price=row[5],
            par_level=row[6]
        ) 
        for row in rows
    ]