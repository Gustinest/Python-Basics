import mysql.connector

cari_data = {}
cari_nama = input("Masukkan Nama Aset: ")

cari_data['nama'] = cari_nama

nama_db = {
    'user': 'root',
    'password': '231103330402',
    'host': 'localhost',
    'database': 'PENDUDUK'
}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

cari_tabel = ("SELECT nama FROM aset_penduduk WHERE nama LIKE %(nama)s")

kursor.execute(cari_tabel, cari_data)
print("Nama aset lama: ")

for column in kursor:
    print(column[0])

print('Pembaruan data')
nama_aset_baru = input("Masukkan Nama Aset Baru: ")

cari_data['nama_baru'] = nama_aset_baru

update_tabel = ("UPDATE aset_penduduk SET nama = %(nama_baru)s WHERE nama = %(nama)s")
kursor.execute(update_tabel, cari_data)
koneksi.commit()
print("Data berhasil diperbarui")

koneksi.close()
