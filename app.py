import sqlite3
from tkinter import Tk, Frame, Label, Button, Entry, StringVar, OptionMenu, messagebox


# === Функция для работы с базой данных ===
def connect_db():
    return sqlite3.connect("partners.db")


# === Получение списка партнеров ===
def get_partners():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, contact_info FROM Partners")
    partners = cursor.fetchall()
    conn.close()
    return partners


# === Функция для добавления/редактирования партнера ===
def save_partner(id=None, name="", partner_type="", rating=0, address="", director="", phone="", email=""):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        if id:
            cursor.execute("""
                UPDATE Partners SET name=?, type=?, rating=?, address=?, director=?, phone=?, email=?
                WHERE id=?
            """, (name, partner_type, rating, address, director, phone, email, id))
        else:
            cursor.execute("""
                INSERT INTO Partners (name, type, rating, address, director, phone, email)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (name, partner_type, rating, address, director, phone, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Успех", "Данные партнера успешно сохранены!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


# === Окно для добавления/редактирования партнера ===
def open_partner_form(id=None):
    def on_save():
        # Получение данных из полей формы
        name = name_var.get()
        partner_type = type_var.get()
        rating = int(rating_var.get()) if rating_var.get().isdigit() else 0
        address = address_var.get()
        director = director_var.get()
        phone = phone_var.get()
        email = email_var.get()

        if not name or not partner_type or not director or not phone or not email:
            messagebox.showwarning("Предупреждение", "Все поля должны быть заполнены!")
            return

        # Сохранение данных
        save_partner(id, name, partner_type, rating, address, director, phone, email)

    # Получаем данные партнера для редактирования, если id передано
    name_var = StringVar()
    type_var = StringVar()
    rating_var = StringVar()
    address_var = StringVar()
    director_var = StringVar()
    phone_var = StringVar()
    email_var = StringVar()

    # Если редактируем, загружаем данные партнера
    if id:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Partners WHERE id=?", (id,))
        partner = cursor.fetchone()
        conn.close()

        if partner:
            name_var.set(partner[1])
            type_var.set(partner[2])
            rating_var.set(partner[3])
            address_var.set(partner[4])
            director_var.set(partner[5])
            phone_var.set(partner[6])
            email_var.set(partner[7])

    # Создаем окно
    form_window = Tk()
    form_window.title("Добавление/Редактирование партнера")

    Label(form_window, text="Наименование:").pack()
    Entry(form_window, textvariable=name_var).pack()

    Label(form_window, text="Тип партнера:").pack()
    partner_types = ["Тип 1", "Тип 2", "Тип 3"]
    OptionMenu(form_window, type_var, *partner_types).pack()

    Label(form_window, text="Рейтинг:").pack()
    Entry(form_window, textvariable=rating_var).pack()

    Label(form_window, text="Адрес:").pack()
    Entry(form_window, textvariable=address_var).pack()

    Label(form_window, text="ФИО директора:").pack()
    Entry(form_window, textvariable=director_var).pack()

    Label(form_window, text="Телефон:").pack()
    Entry(form_window, textvariable=phone_var).pack()

    Label(form_window, text="Email:").pack()
    Entry(form_window, textvariable=email_var).pack()

    Button(form_window, text="Сохранить", command=on_save).pack()
    Button(form_window, text="Закрыть", command=form_window.destroy).pack()

    form_window.mainloop()


# === Главное окно ===
def main_window():
    window = Tk()
    window.title("Список партнеров")

    # Отображаем список партнеров
    partners = get_partners()

    for partner in partners:
        partner_id, partner_name, partner_contact = partner
        frame = Frame(window)
        frame.pack(fill="x", padx=10, pady=5)

        Label(frame, text=f"{partner_name} | {partner_contact}").pack(side="left")

        Button(frame, text="Редактировать", command=lambda id=partner_id: open_partner_form(id)).pack(side="right")

    Button(window, text="Добавить партнера", command=open_partner_form).pack(pady=10)

    window.mainloop()


# Запуск главного окна
main_window()
