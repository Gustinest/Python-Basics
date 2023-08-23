import math

def  main():
    print('Menghitung luas lingkaran')
    radius = float(input('jari jari\t: '))

    luas = math.pi * (radius ** 2)

    print ('\nLuas = ', luas)

if __name__ == '__main__':
    main()
