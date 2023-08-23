import mysql.connector

nama_db = {
    'user':'root', 
    'password' : '231103330402', 
    'host' :'localhost', 
    'database' :'aset'}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute('SHOW TABLES')

for (table_name,) in kursor:
    print(table_name)