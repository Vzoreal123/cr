import sqlite3
import csv

# Подключение к БД
conn = sqlite3.connect("partners.db")
cur = conn.cursor()

# Очистка таблицы
cur.execute("DELETE FROM Partners")
cur.execute("DELETE FROM Product")
cur.execute("DELETE FROM Sales")

# Импорт из CSV
with open("partners.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Пропустить заголовок
    for row in reader:
        cur.execute("INSERT INTO Partners (id, name, contact_info) VALUES (?, ?, ?)", row)

# Сохранение и закрытие
conn.commit()
conn.close()

print("Импорт завершён.")
