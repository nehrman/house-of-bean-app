import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS products
                 (id INTEGER PRIMARY KEY, name TEXT, price REAL)''')
    c.execute("INSERT OR IGNORE INTO products (id, name, price) VALUES (1, 'Espresso', 2.5)")
    c.execute("INSERT OR IGNORE INTO products (id, name, price) VALUES (2, 'Latte', 3.0)")
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT name, price FROM products")
    products = [{"name": row[0], "price": row[1]} for row in c.fetchall()]
    conn.close()
    return products