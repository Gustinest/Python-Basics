def main():
    print('Masukan data diri anda')
    nama = input('Nama\t\t: ')
    alamat = input('Alamat\t\t: ')
    telepom = input('No telepon\t: ')
    
    print('\nData diri: %s, %s, %s' % (nama, alamat, telepom))

    print('\ntype(nama)\t: %s' % type(nama))
    print('ype(alamat)\t: %s' % type(alamat))
    print('type(telepon)\t: %s' % type(telepom))

if __name__ == '__main__':
    main()