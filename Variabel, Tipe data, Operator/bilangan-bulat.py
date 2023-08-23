a = float(input('Masukkan angka a: '))

print(type(a))

m = input('Masukkan Pilihan = 1/2/3: ')

if m in ['1', '2', '3']:
    if m == '1':
        angka_base = bin(int(a))
        print('Angka basenya: ', angka_base)
    elif m == '2':
        angka_base = oct(int(a))
        print("Bilangan oktal:", angka_base)
    elif m == '3':
        angka_base = hex(int(a))
        print("Bilangan hexadecimal:", angka_base)
else:
    print("\n===== Bilangan Pecahan FLOAT =====")
    angka_float = a
    print("Angka float yang ditulis langsung: ", angka_float)
