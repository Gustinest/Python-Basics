class segitiga:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

    @property
    def luas(self):
        return (self.alas * self.tinggi) / 2
    
def main():
    obj = segitiga(6,5)

    print('Luas segitiga = %.2f' % obj.luas)

if __name__ == '__main__':
    main()