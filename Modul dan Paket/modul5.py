import constan 
import writer

def kali(a, b):
    return a * b

def main():
    writer.printA()
    writer.printB()
    print('A x B = %d' % kali(constan.A, constan.B))

if __name__ == '__main__':
    main()