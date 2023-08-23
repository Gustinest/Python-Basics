import shutil

def main():
    lokasi = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\data.txt'
    lokasi1 = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\databack.txt'
    # emebuka file
    # emebuka file
    utama = lokasi
    backup = lokasi1

    shutil.copyfile(utama, backup)

if __name__ == '__main__':
    main()