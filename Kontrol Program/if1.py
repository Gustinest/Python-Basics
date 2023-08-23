import sys
a = float(input('Masukan nilai a: '))
b = float(input('Masukan niali b: '))

if b == a:
    print('Salah: nilai b tidak oleh nol/0. ')
    sys.exit(1)

c = a/b
print('\n %2f / %2f = %2f' % (a,b,c))