import sqlite3

conn = sqlite3.connect("partners.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS Partners (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    contact_info TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Sales (
    id INTEGER PRIMARY KEY,
    partner_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    sale_date DATE,
    quantity INTEGER,
    FOREIGN KEY (partner_id) REFERENCES Partners(id),
    FOREIGN KEY (product_id) REFERENCES Products(id)
)
""")

# Добавим примеры данных
cur.executemany("INSERT INTO Partners (name, contact_info) VALUES (?, ?)", [
    ("Партнёр А", "+7 111 111 11 11"),
    ("Партнёр Б", "+7 222 222 22 22")
])

cur.executemany("INSERT INTO Sales (partner_id, product_id, sale_date, quantity) VALUES (?, ?, ?, ?)", [
    (1, 1, "2024-01-01", 5000),
    (1, 1, "2024-02-01", 10000),
    (2, 1, "2024-03-01", 60000),
])

conn.commit()
conn.close()
