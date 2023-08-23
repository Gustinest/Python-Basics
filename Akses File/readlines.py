def main():
    lokasi = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\data.txt'
    # emebuka file
    f = open(lokasi, 'r')

    data = f.readlines()

    print(data)

    f.close()

if __name__ == '__main__':
    main()