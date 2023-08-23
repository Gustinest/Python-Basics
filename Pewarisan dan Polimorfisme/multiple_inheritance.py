class A:
    def __init__(self, a):
        self.__a = a

    def cetakA(self):
        print('Nilai a: %d' % self.__a)

class B:
    def __init__(self, b):
        self.__b = b

    def cetakB(self):
        print('Nilai b: %d' % self.__b)

class C(A, B):
     def __init__(self, a, b, c):
            # Memanggil metode __init__() pada kelas induk pertama
        A.__init__(self,a)

        B.__init__(self, b)

        self.__c =c
     def cetakC(self):
        print('Nilai c: %d' % self.__c)

def main():
    # membuat objek darri kelas anak
    obj = C(1000, 2000, 3000)

    # Memanggil metode catakA,B,C
    obj.cetakA()
    obj.cetakB()
    obj.cetakC()

if __name__ == '__main__':
    main()
