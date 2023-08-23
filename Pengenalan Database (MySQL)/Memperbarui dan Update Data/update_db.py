import mysql.connector

nama_db = {
    'user': 'root',
    'password': '231103330402',
    'host': 'localhost',
    'database': 'PENDUDUK'
}

print("Koneksi telah berhasil dilakukan")

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

kursor.execute("""UPDATE `aset_penduduk` SET `merek` = 'KIN' WHERE `nama` = 'GOJO'""")

koneksi.commit()
print("Data berhasil diupdate")

koneksi.close()
