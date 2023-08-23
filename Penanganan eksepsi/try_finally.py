f = None
lokasi1 = 'D:\Phyton\Book 5 Tahap\Bab 6 Akses File\datarename.txt'

try:
    f = open(lokasi1)
    data = f.read()
    print(data)
finally:
    if f is not None:
        f.close()