import mysql.connector

nama_db = {
    'user' : 'root',
    'password' : '231103330402', 
    'host' :'localhost', 
    'database' :'PENDUDUK'}

print ("Koneksi telah berhasil dilakukan")

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute("""INSERT INTO aset_penduduk VALUE ('11221', 'BRANKAS', '2016/11/23', 'Rhino', 50000.00);""")

koneksi.commit()
print ("Data telah berhasil dibuat")
koneksi.close