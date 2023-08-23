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

kursor.execute("""DELETE FROM aset_penduduk WHERE nama='KTM' OR merek='Rhino'""")

koneksi.commit()
print('DATA BERHASEL DIHAPUS')

koneksi.close()