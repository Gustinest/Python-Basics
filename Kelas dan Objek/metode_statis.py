class Segitiga:
    def __init__(self, a, t):
        """
        Constructor untuk inisialisasi objek Segitiga dengan alas (a) dan tinggi (t).
        """
        self.alas = a
        self.tinggi = t

    def luas(self):
        """
        Menghitung luas segitiga.
        Formula: luas = (alas * tinggi) / 2
        """
        return (self.alas * self.tinggi) / 2

    def cetakluas(self):
        """
        Menampilkan luas segitiga ke layar dengan format angka desimal dua digit.
        """
        print('Luas segitiga = %.2f' % self.luas())

    @staticmethod
    def daftarAtribut():
        """
        Metode statis untuk mengembalikan daftar atribut dari kelas Segitiga.
        """
        return ('alas', 'tinggi')

def main():
    # Memanggil metode statis daftarAtribut() dari kelas Segitiga.
    print('Daftar atribut dari kelas Segitiga: %s' % repr(Segitiga.daftarAtribut()))

if __name__ == '__main__':
    main()
