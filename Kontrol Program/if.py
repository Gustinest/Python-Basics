def main():
    c = input('Masukan huruf: ')[0].lower()

    if c in ['a','e', 'u', 'i', 'o']:
        print (c, 'Adalah huruf vokal')

if __name__ == '__main__':
    main()