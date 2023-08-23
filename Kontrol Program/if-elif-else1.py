def main():
    no = int(input("Masukan nomor hari 1 sampai 7: "))

    if no == 1:
        print("senin")
    elif no == 2:
        print('Selasa')
    elif no == 3:
        print('Rabu')
    elif no == 4:
        print('Kamis')
    elif no == 5:
        print('Jumau')
    elif no == 6:
        print('sabtu')
    elif no == 7:
        print('Minggu')
    else:
        print("masukan nomor yang benar")

if __name__ == '__main__':
    main()