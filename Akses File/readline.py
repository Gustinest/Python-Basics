def main():
    lokasi = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\data.txt'
    # emebuka file
    f = open(lokasi, 'r')

    # membaca data pertama
    baris1 = f.readline()

    # membaca data kedua
    baris2 = f.readline()

    # membaca data ketiga
    baris3 = f.readline()

     # membaca data ketiga
    baris4 = f.readline()

    #menampilkan data
    print(baris1, end=' ')
    print(baris2, end=' ')
    print(baris3, end=' ')
    print(baris3, end=' ')
    
    # Menutup file
    f.close()

if __name__ == '__main__':
    main()