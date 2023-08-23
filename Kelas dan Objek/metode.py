class segitiga:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t
    
    # Metode untuk menghitung luas
    def luas(self):
        return (self.alas * self.tinggi) / 2

def main():
    # membuat objek dari kelas segitiga
    obj = segitiga(5, 3)

    print('Luas segitiga = %.2f' % obj.luas)

if __name__ == '__main__':
    main()