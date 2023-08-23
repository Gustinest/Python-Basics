import m1
import m2
import m3
import m4
options = """
1. Bilangan Bulat
2. Menghitung Luas Persegi Panjang
3. Menghitung Luas Lingkaran
4. Info Type Value
5. Menghitung Luas
6. Membuat bilangan rentang genap (ARITMATIKA)
7. Membuat bilangan rentang genap (PENUGASAN)
"""

print(options)

pilih = input('Masukan menu yang akan dieksekusi: ')
if pilih in ['1', '2', '3', '4', '5', '6', '7']:
    if pilih == '1':
        a = float(input('Masukan angka: '))
        print('Bilangan binernya:', m1.bilangan_hex(a))
        print('Bilangan binernya:', m1.bilangan_oct(a))
        print('Bilangan binernya:', m1.bilangan_bin(a))

    elif pilih == '2':
        a = float(input('Masukan panjang: '))
        b = float(input('Masukan lebar: '))
        print('Luasnya adalah ', m2.pp(a, b))

    elif pilih == '3':
        a = float(input('Masukan angka: '))
        print('Luas lingkarannya adalah: ', m3.ll(a) )

    elif pilih == '4':
        print('Masukan data diri anda')
        nama = input('Nama\t\t: ')
        alamat = input('Alamat\t\t: ')
        telepom = int(input('No telepon\t: '))
        
        print('\nData diri: %s, %s, %s' % (nama, alamat, telepom))

        print('\ntype(nama)\t: %s' % type(nama))
        print('ype(alamat)\t: %s' % type(alamat))
        print('type(telepon)\t: %s' % type(telepom))

    elif pilih == '5':
        a = float(input('Masukan alas: '))
        b = float(input('Masukan alas: '))
        print('Luasnya adalah: ', m4.luas(a, b))

    elif pilih == '6':
        for i in range(21):
            if i % 2 == 0:
                print(i, end=" ")

    elif pilih == '7':
        i = 0
        while i <= 20:
         print(i, end=' ')
         i += 2

else:
    print("DIPILIH NGAB")