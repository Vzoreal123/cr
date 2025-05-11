import sqlite3
from tkinter import Tk, Frame, Label, LEFT, RIGHT, TOP, BOTH, X

# === Расчет скидки по количеству проданных товаров ===
def calculate_discount(total_quantity):
    if total_quantity < 10000:
        return 0
    elif total_quantity < 50000:
        return 5
    elif total_quantity < 300000:
        return 10
    else:
        return 15

# === Получение списка партнеров и их продаж ===
def get_partners_from_db():
    conn = sqlite3.connect("partners.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.id, p.name, p.contact_info, COALESCE(SUM(s.quantity), 0) AS total_quantity
        FROM Partners p
        LEFT JOIN Sales s ON p.id = s.partner_id
        GROUP BY p.id
    """)

    result = cursor.fetchall()
    conn.close()
    return result

# === Отображение партнёров ===
def display_partners():
    partner_list = get_partners_from_db()

    for partner in partner_list:
        pid, name, contact, total = partner
        discount = calculate_discount(total)

        # Визуальный блок
        frame = Frame(root, relief="solid", borderwidth=1, padx=10, pady=5)
        frame.pack(padx=10, pady=5, fill=X)

        # Верхняя строка: название + скидка
        top_line = Frame(frame)
        top_line.pack(fill=X)

        Label(top_line, text=f"Тип | {name}", font=('Arial', 12, 'bold')).pack(side=LEFT)
        Label(top_line, text=f"{discount}%", font=('Arial', 12)).pack(side=RIGHT)

        # Инфо о контакте, директоре и рейтинге
        Label(frame, text="Директор", font=('Arial', 10)).pack(anchor='w')
        Label(frame, text=contact, font=('Arial', 10)).pack(anchor='w')
        Label(frame, text="Рейтинг: 10", font=('Arial', 10)).pack(anchor='w')

# === Главное окно ===
root = Tk()
root.title("Партнеры компании")

display_partners()

root.mainloop()
