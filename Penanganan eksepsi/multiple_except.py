filename = input('Masukan nama file data: ')
abbr = input('Masukan singkatan yang dicari: ').upper()

try:
    f = open(filename)  # Membuka file dengan nama yang diberikan
    lst = f.read().split('\n')[:-1]  # Membaca isi file dan memisahkan setiap baris menjadi elemen dalam daftar

    data = {}  # Inisialisasi kamus kosong untuk menyimpan pasangan kunci dan nilai dari file
    for e in lst:  # Looping untuk setiap elemen dalam daftar
        key, val = e.split('=')  # Memisahkan pasangan kunci dan nilai menggunakan '=' sebagai pemisah
        data[key] = val  # Menambahkan pasangan kunci dan nilai ke dalam kamus 'data'

    print('\n%s Singkatan dari %s' %(abbr, data[abbr]))  # Mencetak nilai yang sesuai dengan singkatan yang dicari dari kamus 'data'

except FileNotFoundError:  # Penanganan kesalahan jika file tidak ditemukan
    print('\nKesalahan: file \'%s\' tidak ditemukan.' % filename)

except KeyError:  # Penanganan kesalahan jika singkatan tidak ditemukan dalam kamus 'data'
    print('\n%s tidak ditemukan.' % abbr)
