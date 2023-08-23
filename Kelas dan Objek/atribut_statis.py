class segitiga:
    # atribut statis
    objectCount = 0

    def __init__(self,a ,t):
        self.alas = a
        self.tinggi = t

        # menaikan nilai atribut statis
        segitiga.objectCount += 1

    def luas(self):
        return (self.alas * self.tinggi) / 2
    
    def cetakLuas(self):
        print('Luas sEGITIGA = %.2f' % self.luas())

def main():
    # Membuat tiga objek dari kelas segitiga
    obj1 = segitiga(6,5)
    obj2 = segitiga(5,4)
    obj3 = segitiga(4,3)

    # Memanggil atribut segitiga.ojectcount
    print('Jumlah objek dari kelas segitiga: %d' % segitiga.objectCount)

if __name__ == '__main__':
    main()