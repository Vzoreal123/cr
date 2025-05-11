import sqlite3
import csv

conn = sqlite3.connect("partners.db")
cur = conn.cursor()

# Очистка таблицы
cur.execute("DELETE FROM Partners")
cur.execute("DELETE FROM Products")
cur.execute("DELETE FROM Sales")

# Импорт Partners
with open("partners.csv", newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовки
    for row in reader:
        cur.execute("INSERT INTO Partners (id, name, contact_info) VALUES (?, ?, ?)", row)

# Импорт Products
with open("products.csv", newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO Products (id, name, description) VALUES (?, ?, ?)", row)

# Импорт Sales
with open("sales.csv", newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cur.execute("INSERT INTO Sales (id, partner_id, product_id, sale_date, quantity) VALUES (?, ?, ?, ?, ?)", row)

conn.commit()
conn.close()
