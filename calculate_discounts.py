import sqlite3

def get_discount(total):
    if total <= 10000:
        return 0
    elif total <= 50000:
        return 5
    elif total <= 300000:
        return 10
    else:
        return 15

conn = sqlite3.connect("partners.db")
cur = conn.cursor()

cur.execute("SELECT id, name, contact_info FROM Partners")
partners = cur.fetchall()

for partner in partners:
    pid, name, contact = partner
    cur.execute("SELECT COALESCE(SUM(quantity), 0) FROM Sales WHERE partner_id = ?", (pid,))
    total = cur.fetchone()[0]
    discount = get_discount(total)
    print(f"{name} | {contact} | Скидка: {discount}%")

conn.close()
