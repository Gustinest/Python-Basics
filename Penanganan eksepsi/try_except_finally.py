f = None  # Inisialisasi variabel objek file dengan None
status = True  # Inisialisasi variabel status dengan True
filename = input('Masukan nama file yang akan dibaca: ')  # Meminta pengguna memasukkan nama file

try:
    f = open(filename)  # Membuka file dengan nama yang diberikan
    data = f.read()  # Membaca isi file
    print(data)  # Mencetak isi file
except FileNotFoundError as e:
    status = False  # Mengubah status menjadi False
    print('Kesalahan: File \'%s\' tidak ditemukan.' % filename)  # Mencetak pesan kesalahan jika file tidak ditemukan
finally:
    if f is not None:  # Memeriksa jika objek file tidak bernilai None
        f.close()  # Menutup file
    if not status:  # Jika status adalah False (terjadi kesalahan)
        print('Operasi dibatalkan')  # Mencetak pesan bahwa operasi dibatalkan
    else:
        print('Operasi Selesai')  # Mencetak pesan bahwa operasi selesai
