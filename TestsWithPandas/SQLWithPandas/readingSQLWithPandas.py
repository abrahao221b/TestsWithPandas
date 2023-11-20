import pandas 
import sqlite3

connection = sqlite3.connect('dabaseTest.db')

cursor = connection.cursor()

cursor.execute('''
    SELECT * FROM supplier
''')

# Tables 
# for table in cursor.fetchall():
#     print(table)

# Reading with pandas

query = "SELECT * FROM supplier"

consult_pandas = pandas.read_sql(query, connection)

print(f"consult_pandas: \n{consult_pandas}")
