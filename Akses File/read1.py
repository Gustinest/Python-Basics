def main():
    lokasi = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\data.txt'
    # Membuka file
    with open(lokasi, 'r') as f:
        # Membaca data
        data = f.read()

        # Mengkonversi data ke dalam bentuk raw string
        rawData = data.encode('unicode-escape')

        # Menampilkan data
        print(rawData)

if __name__ == '__main__':
    main()

