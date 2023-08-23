import mysql.connector

cari_data = {}
cari_nama = input("Masukan nama aset: ")

cari_data['nama'] = "%" + cari_nama + "%"

nama_db = {
    'user' : 'root',
    'password' : '231103330402', 
    'host' :'localhost', 
    'database' :'PENDUDUK'}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

cari_tabel = ("""SELECT * FROM aset_penduduk WHERE nama LIKE %(nama)s""")

kursor.execute(cari_tabel, cari_data)

print ("Kode"), print ("nama"), print ("Tanggal beli"), print ("Merek"), print ("nilai")

for (column) in kursor:
    print(column[0]), print(column[1]), print(column[2]), print(column[3]), print(column[4])

koneksi.close()