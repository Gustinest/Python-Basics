import mysql.connector

nama_db = {
    'user':'root', 
    'password' : '231103330402', 
    'host' :'localhost', 
    'database' :'aset'}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute('DESC aset_kantor')

for (column) in kursor:
    print (column[0]),
    print (column[1])