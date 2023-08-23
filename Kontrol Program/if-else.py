def main():
    a = float(input('masukan nilai a: '))
    b = float(input('masukan nilai b: '))

    if b == 0:
        print('salah: nilai b tidak boleh 0')
    else:
        c = a/b
        print('\n%2f / %2f = %2f' % (a,b,c))

if __name__ == '__main__':
    main()
