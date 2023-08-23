def main():
    lokasi = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\data.txt'
    # emebuka file
    with open(lokasi, 'r') as f:

        data = f.read()

        print(data)

    f.close()

if __name__ == '__main__':
    main()