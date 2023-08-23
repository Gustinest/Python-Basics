import mysql.connector

nama_db = {
    'user' : 'root',
    'password' : '231103330402', 
    'host' :'localhost', 
    'database' :'PENDUDUK'}

print ("Koneksi telah berhasil dilakukan")

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute("""SELECT * FROM aset_penduduk""")

print ("Kode"), print ("nama"), print ("Tanggal beli"), print ("Merek"), print ("nilai")

for (column) in kursor:
    print(column[0]), print(column[1]), print(column[2]), print(column[3]), print(column[4])

koneksi.close()