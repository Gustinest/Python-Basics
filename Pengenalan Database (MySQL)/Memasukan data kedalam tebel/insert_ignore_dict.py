from __future__ import print_function
from datetime import date, datetime, timedelta
import mysql.connector

data_PENDUDUK = {
    'kode': '540111111',
    'nama': 'Superdi',
    'tgl_beli': date(2045, 11, 23),
    'merek': 'SAMSUNG',
    'nilai': 1231122100
}

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

kursor.execute(tambah_db, data_PENDUDUK)

koneksi.commit()
koneksi.close()
