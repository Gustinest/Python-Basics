import mysql.connector

nama_db = {
    'user':'root', 
    'password' : '231103330402', 
    'host' :'localhost', 
    'database' :'aset'}

print ("Koneksi telah berhasil dilakukan")

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()
kursor.execute(""" CREATE TABLE aset_kantor2 ( kode char(9), nama char(15), tgl_beli date, merek char(10), nilai decimal(15,2))""")

koneksi.commit()
print ("tabel telah berhasil dibuat")
koneksi.close