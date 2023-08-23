import math

# fungsi bagian luar
def luaslingkaran(r):
    # fungsi lokal
    def kuadrat(x):
        return x ** 2
    # Memanggill fungsi lokal dari fungsi bagian luar
    return math.pi * kuadrat(r)

def main():
    r = float(input('Masukan jari jari lingkaran: '))
    luas = luaslingkaran(r)

    print('Luas lingkaran = %.3f' % luas)

if __name__ == '__main__':
    main()

# import math: Ini adalah pernyataan impor yang mengimpor modul math yang menyediakan fungsi matematika yang lebih kompleks, termasuk nilai pi.

# def luaslingkaran(r):: Ini adalah definisi fungsi luaslingkaran() yang menerima parameter r yang merupakan jari-jari lingkaran.

# def kuadrat(x):: Ini adalah definisi fungsi lokal kuadrat() yang menerima parameter x dan mengembalikan nilai kuadrat dari x (x^2).

# return math.pi * kuadrat(r): Pada fungsi luaslingkaran(), nilai dari jari-jari r dikalikan dengan hasil panggilan fungsi lokal kuadrat() untuk menghitung luas lingkaran. Fungsi lokal kuadrat() dipanggil dengan argumen r, dan kemudian hasilnya dikalikan dengan math.pi yang merupakan konstanta pi dari modul math. Nilai luas lingkaran ini kemudian dikembalikan sebagai hasil fungsi luaslingkaran().

# def main():: Ini adalah definisi fungsi main() yang digunakan untuk menjalankan kode utama.

# r = float(input('Masukan jari jari lingkaran: ')): Di dalam fungsi main(), pengguna diminta untuk memasukkan jari-jari lingkaran melalui input. Nilai yang dimasukkan oleh pengguna diubah menjadi float menggunakan fungsi float() dan disimpan dalam variabel r.

# luas = luaslingkaran(r): Nilai r kemudian digunakan sebagai argumen saat memanggil fungsi luaslingkaran(), dan hasilnya disimpan dalam variabel luas.

# print('Luas lingkaran = %.3f' % luas): Akhirnya, hasil luas lingkaran dicetak ke layar dengan menggunakan string format %.3f untuk memformat angka desimal dengan tiga angka di belakang koma.