def bagi(a, b):
    # Memeriksa tipe data a dan b
    if not (isinstance(a, float) or isinstance(a, int)):
        raise ValueError('Nilai a harus bertipe bilangan')
    if not (isinstance(b, float) or isinstance(b, int)):
        raise ValueError('Nilai b harus bertipe bilangan')
    
    # Memeriksa apakah b adalah nol
    if b == 0:
        raise ZeroDivisionError('')

    return a / b

def main():
    try:
        # Memanggil fungsi bagi dengan argumen 6.0 dan 3
        c = bagi(6.0, 3)
        print(c)

    except ValueError as e:
        print(e)

    except ZeroDivisionError as e:
        print(e)

if __name__ == '__main__':
    main()
