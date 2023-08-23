import sys
print('PROGRAM PEMBAGIAN BILANGAN')

a = float(input('Masukan nilai a: '))
b = float(input('Masukan nilai b: '))

if b == 0:
    print('\nsalah: nilai b tidak boleh 0')
    sys.exit(1)

print('\n%.3f / %.3f = %.3f' % (a, b, a / b))

# % : Tanda persen awal menandakan bahwa akan ada penggantian nilai yang dilakukan menggunakan operator modulo.
# .3 : Bagian ini mengatur presisi desimal. Dalam contoh ini, angka 3 menunjukkan bahwa akan ada 3 angka di belakang koma.
# f : Huruf 'f' menunjukkan bahwa nilai yang akan digantikan adalah float (angka desimal).