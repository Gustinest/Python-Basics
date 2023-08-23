import aritmatika

def main():
    a = int(input('Masukan nilai a: '))
    b = int(input('Masukan nilai b: '))
    c = float(b)

    print('a\t: %d' % a)
    print('b\t: %d' % b)
    print('c\t: %.2f' % c)

    print('a + b\t: %d' % aritmatika.tambah(a,b))
    print('a - b\t: %d' % aritmatika.kurang(a,b))
    print('a * b\t: %d' % aritmatika.kali(a,b))
    print('a // b\t: %d' % aritmatika.bagi(a,b))
    print('a / b\t: %f' % aritmatika.bagi(a,b))
    print('a sisabagi b\t: %d' % aritmatika.sisabagi(a,b))
    print('a ** b\t: %d' % aritmatika.pangkat(a,b))

if __name__=='__main__':
    main()