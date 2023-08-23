def kali(a, b):
    return a * b

def bagi (a, b):
    return a / b

def main():
    print("Program Perkalian Billangan")
    a = float(input('Masukan nilai a: '))
    b = float(input('Masukan nilai b: '))

    print('%.2f * %.2f = %.3F ' % (a, b, kali(a, b)))
    print('%.3f / %.3f = %.3F ' % (a, b, bagi(a, b)))

if __name__ == '__main__':
    main()