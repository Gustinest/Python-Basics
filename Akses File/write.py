def main():

    lokasi = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\data.txt'
    # emebuka file
    f = open(lokasi, 'w')

    # menulis data ke dalam file
    f.write('Phyton\n')
    f.write('C++\n')
    f.write('PHP\n')
    f.write('PHP\n')

    # Menutup file
    f.close()

if __name__ == '__main__':
    main()