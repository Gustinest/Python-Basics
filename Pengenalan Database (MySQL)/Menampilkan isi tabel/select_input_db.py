import mysql.connector

cari_data = {}
cari_kode = input("Masukan kode: ")
cari_data['kode'] = cari_kode

nama_db = {
    'user' : 'root',
    'password' : '231103330402', 
    'host' :'localhost', 
    'database' :'PENDUDUK'}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

cari_tabel = ("""SELECT * FROM aset_penduduk WHERE kode= %(kode)s""")

kursor.execute(cari_tabel, cari_data)

print ("Kode"), print ("nama"), print ("Tanggal beli"), print ("Merek"), print ("nilai")

for (column) in kursor:
    print(column[0]), print(column[1]), print(column[2]), print(column[3]), print(column[4])

koneksi.close()