class segitiga:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

def main():
    # membuat objek dari kelas segitiga
    obj = segitiga(5, 3)

    # menggunakan atribut untuk perhitungan
    luas = (obj.alas * obj.tinggi) / 2

    print('Luas segitiga = %.2f' % luas)

if __name__ == '__main__':
    main()