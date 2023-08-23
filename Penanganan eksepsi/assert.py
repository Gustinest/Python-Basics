a = float(input('Masukan nilai a: '))
b = float(input('Masukan nilai b: '))

assert b != 0, 'Kesalahan: nilai b tidak boleh 0'

c = a / b
print('%.3f / %.3f = %.3f' % (a,b,c))