class A:
    def __init__(self, a):
        self.__a = a

    def B(self, b):
        self.__b = b

    def cetakNilai(self):
        print('Nilai a: %d' % self.__a)

class B(A):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.__b = b
        self.__c = c

    def cetakNilai(self):
        super().cetakNilai()
        print('Nilai b: %d' % self.__b)
        print('Nilai c: %d' % self.__c)

def main():
    obj1 = A(100)
    print('Memanggil cetakNilai() dari kelas A')
    obj1.cetakNilai()

    obj2 = B(1000, 2000, 3000)
    print('Memanggil cetakNilai() dari kelas B')
    obj2.cetakNilai()

if __name__ == '__main__':
    main()
