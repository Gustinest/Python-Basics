from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

data_aset = {}

kode_aset = input("Masukan kode aset: ")
nama_aset = input('masukan nama aset: ')
merek_aset = input("masukan merk aset: ")
nilai_aset = float(input("Masukan harga aset: "))

data_aset['kode'] = kode_aset
data_aset['nama'] = nama_aset
data_aset['tgl_beli'] = datetime.now().date()
data_aset['merek'] = merek_aset
data_aset['nilai'] = nilai_aset

nama_db = {
    'user': 'root',
    'password': '231103330402', 
    'host': 'localhost', 
    'database': 'PENDUDUK'
}

koneksi = mysql.connector.connect(**nama_db)
kursor = koneksi.cursor()

tambah_db = ("INSERT INTO aset_penduduk "
             "(kode, nama, tgl_beli, merek, nilai) "
             "VALUES (%(kode)s, %(nama)s, %(tgl_beli)s, %(merek)s, %(nilai)s)")

kursor.execute(tambah_db, data_aset)

koneksi.commit()
koneksi.close()
