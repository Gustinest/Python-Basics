class segitiga:
    def __init__(self, a, t):
        self.__alas = a
        self.__tinggi = t

    @property
    def alas(self):
        return self.__alas
    
    @alas.setter
    def alas(self, a):
        self.__alas = a

    # @property adalah decorator di Python yang mengubah method menjadi properti. alas adalah properti yang memungkinkan akses hanya untuk membaca atribut __alas.
    # @alas.setter adalah setter method untuk properti alas. Ini memungkinkan penggunaan obj.alas = nilai untuk mengubah nilai atribut __alas.    
    
    @property
    def tinggi(self):
        return self.__tinggi
    
    @tinggi.setter
    def tinggi(self, t):
        self.__tinggi = t

    @property
    def luas(self):
        return(self.alas * self.tinggi) / 2
    

def  main():
    # Membuat objek dari kelas segitiga
    obj = segitiga(6,5)

    print('SEBELUM DIUBAH')
    print('Alas = %.2f' % obj.alas)
    print('tinggi = %.2f' % obj.tinggi)
    print('Luas Segitiga = %.2f' % obj.luas)

    # Mengubah nilai atribut melalui properti
    obj.alas = 8
    obj.tinggi = 6

    print ('Setelah Diubah: \n')
    print('Alas = %.2f' % obj.alas)
    print('tinggi = %.2f' % obj.tinggi)
    print('Luas Segitiga = %.2f' % obj.luas)


if __name__ == '__main__':
    main()