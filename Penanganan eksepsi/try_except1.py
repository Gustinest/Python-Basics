a = float(input('Masukan nilai a: '))
b = float(input('Masukan nilai b: '))

try:
    c = a / b
except ZeroDivisionError as e:
    print(e)

else:
    print('%.2f / %.2f = %.2f' % (a, b, c))