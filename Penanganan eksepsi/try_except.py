a = float(input('Masukan nilai a: '))
b = float(input('Masukan nilai b: '))

try:
    c = a / b
except ZeroDivisionError as e:
    print(e)
    import sys
    sys.exit(1) # menghentikan eksekusi program

# tidak akan dieksekusi jika terjadi kesalahan
print('%.2f / %.2f = %.2f' % (a, b, c))