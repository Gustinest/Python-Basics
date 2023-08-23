def jumlah(*args):
    if args is None: return  0.0
    total = 0.0
    for a in args:
        total += a
    return total

def main():
    print('1 + 2 + 3 + 4 + 5 = %d ' % jumlah(1 + 2 + 3 + 4 + 5))

if __name__ == '__main__':
    main()

# Kodingan di atas adalah contoh dari sebuah fungsi jumlah() yang menerima argumen dalam bentuk *args (artinya argumen dapat berjumlah variabel). Fungsi ini digunakan untuk menjumlahkan semua nilai yang diberikan sebagai argumen dan mengembalikan total jumlahnya.

# Berikut adalah penjelasan dari setiap bagian kode:

# def jumlah(*args):: Ini adalah definisi dari fungsi jumlah() yang menggunakan *args sebagai parameter. Parameter *args memungkinkan fungsi untuk menerima sejumlah argumen yang berbeda dan menyimpannya dalam bentuk tupel.

# if args is None: return 0.0: Pemeriksaan kondisi ini memeriksa apakah argumen *args yang diberikan ke fungsi adalah None atau tidak ada. Jika iya, artinya tidak ada argumen yang diberikan, maka fungsi akan mengembalikan 0.0.

# total = 0.0: Variabel total digunakan untuk menyimpan hasil penjumlahan dari argumen-argumen yang diberikan.

# for a in args: total += a: Ini adalah loop for yang digunakan untuk mengiterasi setiap elemen dalam *args. Setiap elemen (disebut sebagai a) ditambahkan ke total menggunakan operator +=, sehingga mengakumulasi jumlah dari semua argumen.

# return total: Setelah selesai mengiterasi semua argumen, fungsi mengembalikan nilai total yang merupakan hasil penjumlahan dari argumen-argumen yang diberikan.

# def main():: Ini adalah definisi dari fungsi main() yang digunakan untuk menjalankan kode utama.

# print('1 + 2 + 3 + 4 + 5 = %d ' % jumlah(1 + 2 + 3 + 4 + 5)): Di dalam fungsi main(), ada satu pernyataan cetak yang mencetak hasil penjumlahan 1 + 2 + 3 + 4 + 5 dengan menggunakan fungsi jumlah(). Ekspresi 1 + 2 + 3 + 4 + 5 dievaluasi terlebih dahulu dan hasilnya diberikan sebagai argumen untuk fungsi jumlah(). Hasilnya diformat menggunakan string format %d dan dicetak.

# if __name__ == '__main__': main(): Ini adalah pengecekan kondisi yang memeriksa apakah skrip dijalankan secara langsung (sebagai program utama) atau diimpor sebagai modul. Jika skrip dijalankan secara langsung, maka fungsi main() akan dipanggil untuk menjalankan kode utama.