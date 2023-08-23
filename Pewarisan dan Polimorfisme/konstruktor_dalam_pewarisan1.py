class A:
    def __init__(self):
        print('A.__init__()')

class B(A):
    def __init__(self):
       # memangggil metode __init__() milik kelas induk
       super().__init__()
       print('B.__init__()')

def main():
    object = B()

if __name__ == '__main__':
    main()