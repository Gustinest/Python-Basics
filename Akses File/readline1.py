def main():
    lokasi = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\data.txt'
    # Membuka file
    with open(lokasi, 'r') as f:
        # Membaca baris pertama
        baris = f.readline()

        while baris:
            # Menampilkan data
            print(baris, end=' ')

            # Membaca baris selanjautnya
            baris = f.readline()

    f.close()
    
if __name__ == '__main__':
    main()

