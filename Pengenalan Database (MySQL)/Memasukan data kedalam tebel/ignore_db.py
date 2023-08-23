import mysql.connector

nama_db = {
    'user' : 'root',
    'password' : '231103330402', 
    'host' :'localhost', 
    'database' :'PENDUDUK'}

print ("Koneksi telah berhasil dilakukan")

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute("""INSERT IGNORE INTO aset_penduduk VALUES ('341231202', 'BAYgon', 20190819, 'REALME', 123000.00),
('98724423', 'WahyudiO', 20111102, 'JUNAIDI', 15000.00), 
('330402', 'IGNORE', 20251124, 'BAGAS', 9888238.00);""")

koneksi.commit ()
print ("Data telah berhasil dibuat")
koneksi.close()