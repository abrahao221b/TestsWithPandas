import sqlite3

connection = sqlite3.connect('dabaseTest.db')

cursor = connection.cursor()

queryString = '''
        SELECT * FROM supplier
'''

cursor.execute(queryString)


for table in cursor.fetchall():
    print(table)
    
    
cursor.close()
connection.close()