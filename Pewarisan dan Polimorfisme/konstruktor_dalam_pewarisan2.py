class A:
    def __init__(self, a):
        print('A.__init__()')
        self.__a = a

    def B(self, b):
        self.__b = b

    def cetakA(self):
        print('Nilai a: %d' % self.__a)

class B(A):
    def __init__(self, a, b, c):
        super().__init__(a)
        print('B.__INIT__()')

        self.__b = b
        print('C.__init__()')
        self.__c = c

    def cetakB(self):
        
        print('Nilai b: %d' % self.__b)
        print('Nilai c: %d' % self.__c)

def main():
    obj = B(1000, 2000, 3000)
    obj.cetakA()
    obj.cetakB()

if __name__ == '__main__':
    main()
