from graphviz import Digraph

# Создаем объект диаграммы
dot = Digraph(comment='ER Diagram for Partner System')

# Таблица Partners
dot.node('Partners', '''{
    Partners |
    id : INTEGER (PK) \l
    name : TEXT \l
    contact_info : TEXT \l
}''', shape='record')

# Таблица Products
dot.node('Products', '''{
    Products |
    id : INTEGER (PK) \l
    name : TEXT \l
    description : TEXT \l
}''', shape='record')

# Таблица Sales
dot.node('Sales', '''{
    Sales |
    id : INTEGER (PK) \l
    partner_id : INTEGER (FK) \l
    product_id : INTEGER (FK) \l
    sale_date : DATE \l
    quantity : INTEGER \l
}''', shape='record')

# Связи
dot.edge('Partners', 'Sales', label='1:N')
dot.edge('Products', 'Sales', label='1:N')

# Сохранение в PDF
dot.render('er_diagram', format='pdf', cleanup=True)
print("✅ ER-диаграмма успешно создана как 'er_diagram.pdf'")
