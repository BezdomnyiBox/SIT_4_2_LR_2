import sqlite3
# создаем базу данных и устанавливаем соединение с ней
con = sqlite3.connect("furniture_company.sqlite")
# открываем файл с дампом базой двнных
f_damp = open('furniture.db','r', encoding ='utf-8-sig')
# читаем данные из файла
damp = f_damp.read()
# закрываем файл с дампом
f_damp.close()
# запускаем запросы
con.executescript(damp)
# сохраняем информацию в базе данных
con.commit()
# создаем курсор
cursor = con.cursor()
# два запроса на выборку для связанных таблиц с условиями и сортировкой;

""" cursor.execute('''SELECT f.furniture_name, f.furniture_price FROM furnitures f
               JOIN types t ON f.furniture_type = t.type_id
               WHERE t.type_name = :p_type_name
               ORDER BY furniture_price
''', {"p_type_name": "Стол"})
print(cursor.fetchall())

cursor.execute('''SELECT cl.client_name, co.check_in_date FROM contracts co
               JOIN clients cl ON co.client_id = cl.client_id
               WHERE co.check_in_date <= :p_check_in_date
               ORDER BY cl.client_name
''', {"p_check_in_date": "2023-09-12"})
print(cursor.fetchall())  """

# два запроса с группировкой и групповыми функциями;

""" cursor.execute('''SELECT client_id, COUNT(*) AS client_id_count
               FROM contracts
               GROUP BY client_id
''')
print(cursor.fetchall())

cursor.execute('''SELECT f.furniture_name, t.type_name, c.color_name, AVG(f.furniture_price) AS avg_price
               FROM furnitures f
               JOIN types t ON t.type_id = f.furniture_type
               JOIN colors c ON c.color_id = f.furniture_color
               GROUP BY f.furniture_price
''')
print(cursor.fetchall()) """

# два запроса со вложенными запросами или табличными выражениями;

""" cursor.execute('''SELECT * FROM furnitures
               WHERE furniture_price > (SELECT AVG(furniture_price) FROM furnitures)
''')
print(cursor.fetchall())

cursor.execute('''SELECT check_in_date, check_out_date, 
        (SELECT client_name FROM clients 
        WHERE clients.client_id = contracts.client_id) AS client_name
        FROM contracts
''')
print(cursor.fetchall()) """

# два запроса корректировки данных (обновление, добавление, удаление и пр)
	
""" cursor.execute('''
               INSERT INTO colors (color_name) VALUES ('Бежевый')
''')
cursor.execute('''
               SELECT * 
               FROM colors
''')
print(cursor.fetchall())


cursor.execute('''
               DELETE FROM colors
               WHERE color_name='Бежевый';
''')
cursor.execute('''
               SELECT * 
               FROM colors
''')
print(cursor.fetchall()) """


# закрываем соединение с базой
con.close()

