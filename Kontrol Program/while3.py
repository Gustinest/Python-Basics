def main():
    a = int(input('Masukan nilai a: '))
    b = int(input('Masukan nilai b: '))

    temp = a
    while a >= b: 
        a -= b

    print('\n%d mod %d = %d ' % (temp, b, a))

if __name__ == '__main__':
    main()
    
'Dalam kode ini, pertama-tama kita meminta pengguna untuk memasukkan nilai a dan b'
'menggunakan fungsi input yang kemudian dikonversi menjadi integer menggunakan' 
'fungsi int(). Kemudian, kita menyimpan nilai awal a dalam variabel temp untuk dicetak nanti'

'Selanjutnya, dalam loop while, kita mengurangi nilai a dengan b sampai a menjadi lebih kecil' 
'dari b. Ini dilakukan untuk mencari sisa dari pembagian a dengan b'

'Terakhir, kita mencetak nilai temp, b, dan a menggunakan format string dengan %d sebagai'
'placeholder untuk nilai integer yang akan digantikan'