def faktorial(n):
    if n == 0: return 1
    return n * faktorial(n-1)

def main():
    n = int(input('Masukan bilangan bulat: '))
    print('%d! = %d' % (n, faktorial(n)))

if __name__ == '__main__':
    main()

# def faktorial(n):: Ini adalah definisi fungsi faktorial() yang menerima parameter n, yang merupakan bilangan bulat yang akan dihitung faktorialnya.

# if n == 0: return 1: Ini adalah pengecekan kondisi untuk menangani kasus dasar dalam rekursi. Jika n sama dengan 0, maka fungsi akan mengembalikan nilai 1, karena faktorial dari 0 adalah 1.

# return n * faktorial(n-1): Ini adalah bagian rekursif dari fungsi. Fungsi faktorial() memanggil dirinya sendiri dengan argumen n-1 dan mengalikan n dengan hasil panggilan rekursif tersebut. Proses ini terus berlanjut sampai mencapai kasus dasar (0!), di mana rekursi akan berhenti dan nilai 1 akan dikembalikan.

# def main():: Ini adalah definisi fungsi main() yang digunakan untuk menjalankan kode utama.

# n = int(input('Masukan bilangan bulat: ')): Di dalam fungsi main(), pengguna diminta untuk memasukkan bilangan bulat melalui input. Nilai yang dimasukkan oleh pengguna diubah menjadi integer menggunakan fungsi int() dan disimpan dalam variabel n.

# print('%d! = %d' % (n, faktorial(n))): Fungsi faktorial() dipanggil dengan argumen n, dan hasilnya dicetak ke layar menggunakan string format %d untuk memformat bilangan bulat. Ini akan mencetak hasil perhitungan faktorial dari bilangan yang dimasukkan.