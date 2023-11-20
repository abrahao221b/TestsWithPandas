import sqlite3

connection = sqlite3.connect('dabaseTest.db')

cursor = connection.cursor()

table = '''
    CREATE TABLE supplier (
        id_supplier INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name_supplier TEXT NOT NULL,
        cnpj VARCHAR(18) NOT NULL,
        city TEXT,
        state VARCHAR(2) NOT NULL,
        zip_code VARCHAR(9) NOT NULL,
        register_date DATE NOT NULL    
    );

'''

cursor.execute(table)

data = [
    ('Empresa D', '44.444.444/4444-44', 'São Paulo', 'SP', '44444-444', '2023-01-01'),

    ('Empresa E', '55.555.555/5555-55', 'São Paulo', 'SP', '55555-555', '2023-01-03'),

    ('Empresa F', '66.666.666/6666-66', 'São Paulo', 'SP', '66666-666', '2023-01-05')

]

cursor.executemany('''
                   INSERT INTO supplier (name_supplier, cnpj, city, state, zip_code, register_date)
                   VALUES(?, ?, ?, ?, ?, ?)
                   ''', data)


connection.commit()

cursor.close()
connection.close()