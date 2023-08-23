import mysql.connector

nama_db = {
    'user' : 'root',
    'password' : '231103330402', 
    'host' :'localhost', 
    'database' :'PENDUDUK'}

print ("Koneksi telah berhasil dilakukan")

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()
kursor.execute("""ALTER TABLE aset_penduduk ADD PRIMARY KEY(kode);""")
koneksi.commit()

kursor.execute("DESC aset_penduduk")

for (column) in kursor:
    print(column[0]),
    print(column[1]),
    print(column[2]),
    print(column[3])

koneksi.close()
