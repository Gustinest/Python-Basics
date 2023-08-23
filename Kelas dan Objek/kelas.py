class Segitiga:
    def __init__(self):
        self.alas = 0.0
        self.tinggi = 0.0

def main():
    # membuat objek dari kelas segitiga
    obj = Segitiga()

    # mengisi nilai kedalam atribut obj
    obj.alas = 5
    obj.tinggi = 3

    # menggunakan atribut untuk perhitungan
    luas = (obj.alas * obj.tinggi) / 2

    print('Luas segitiga = %.2f' % luas)

if __name__ == '__main__':
    main()
