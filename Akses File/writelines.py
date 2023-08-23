
def main():
    # Menentukan lokasi penyimpanan file
    lokasi = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\data1.txt'

    # Membuka file
    f = open(lokasi, 'w')

    data = ['Python\n', 'C++\n']
    # Menulis data ke dalam file
    f.writelines(data)

    # Menutup file
    f.close()

if __name__ == '__main__':
    main()
