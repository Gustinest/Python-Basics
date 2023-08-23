import sys

hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

no = int(input("Masukan nomor hari 1 sampai 7: "))

if no < 1 or no > 7:
    print('Nilai yang dimasukan salah')
    sys.exit(1)

print(hari[no-1])

