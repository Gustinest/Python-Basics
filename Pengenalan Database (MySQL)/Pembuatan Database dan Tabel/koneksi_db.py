import mysql.connector

koneksi = mysql.connector.connect(user='root', password='231103330402', host='localhost', database='aset')

print ("Koneksi telah berhasil dilakukan")
koneksi.close