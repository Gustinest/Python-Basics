def f(n):
    import time
    if n == 0:
        print('GO')
        return
    print(n, end=' ')
    time.sleep(1)
    f(n-1) #memanggil dirinya sendiri

f(3)
f(10)

if __name__ == '__f__':
    f()

# import time: Ini adalah pernyataan impor yang mengimpor modul time yang digunakan untuk mengatur jeda waktu dalam detik.

# if n == 0: print('GO'); return: Ini adalah pengecekan kondisi untuk menangani kasus dasar dalam rekursi. Jika n sama dengan 0, maka fungsi akan mencetak 'GO' dan mengembalikan nilai, menghentikan rekursi.

# print(n, end=' '): Pada setiap iterasi, angka n dicetak menggunakan fungsi print(). Argumen end=' ' digunakan untuk menentukan bahwa setelah mencetak angka, karakter spasi (' ') akan dicetak sebagai pemisah antara angka-angka yang dicetak. Ini berarti angka-angka tersebut akan dicetak dalam satu baris.

# time.sleep(1): Ini adalah pernyataan yang memberikan jeda waktu selama 1 detik menggunakan fungsi sleep() dari modul time. Ini akan membuat program berhenti selama 1 detik sebelum melanjutkan ke iterasi berikutnya.

# f(n-1): Pada setiap iterasi, fungsi f() memanggil dirinya sendiri dengan argumen n-1, sehingga menciptakan rekursi. Ini akan melanjutkan mencetak angka-angka dalam urutan menurun hingga mencapai kasus dasar.

# f(3): Pemanggilan fungsi f() dengan argumen 3 akan mencetak angka 3, 2, 1, dan akhirnya 'GO' secara berurutan dengan jeda waktu 1 detik antara setiap pencetakan.

# f(10): Pemanggilan fungsi f() dengan argumen 10 akan mencetak angka 10, 9, 8, ..., 1, dan akhirnya 'GO' secara berurutan dengan jeda waktu 1 detik antara setiap pencetakan.