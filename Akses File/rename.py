import os

def main():
    lokasi = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\data1.txt'
    lokasi1 = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\datarename.txt'
    
    oldname = lokasi
    newname = lokasi1

    os.rename(oldname, newname)

if __name__ == '__main__':
    main()