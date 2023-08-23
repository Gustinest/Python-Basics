def main():
    a = int(input('masukan bilangan bulat: '))

    if a > 0:
        print('Bilangan positif')
    elif a == 0:
        print('Anda memasukan nilai 0')
    else:
        print('Adalah bilangan negatif')

if __name__ == '__main__':
    main()