class segitiga:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t
    
    # Metode untuk menghitung luas
    def luas(self):
        return (self.alas * self.tinggi) / 2
    
    # Metode untuk mencetak luas 
    def cetakluas(self):
        print('Luas segitiga = %.2f' % self .luas())

def main():
    # membuat objek dari kelas segitiga
    obj = segitiga(5, 3)

    # Memanggil metode cetak luas
    obj.cetakluas()

if __name__ == '__main__':
    main()