def main ():
    a = 13
    b = 45.67

    print ('Sebelum diubah: ')
    print ('Nilai a\t\t: ', a)
    print ('Nilai b\t\t: ', b)
    print ('Tipe data a\t: ', type (a))
    print ('Tipe data b\t: ', type (b))
    print ('Identitas a\t: ', id(a))
    print ('Identitas b\t: ', id(b))

    a = 'Python'
    b = True

    print ('Sesudah diubah: ')
    print ('Nilai a\t\t: ', a)
    print ('Nilai b\t\t: ', b)
    print ('Tipe data a\t: ', type (a))
    print ('Tipe data b\t: ', type (b))
    print ('Identitas a\t: ', id(a))
    print ('Identitas b\t: ', id(b))

if __name__ == "__main__":
    main()
