import os

def main():
    lokasi1 = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\databack.txt'
    
    filename = lokasi1

    os.remove(filename)

if __name__ == '__main__':
    main()