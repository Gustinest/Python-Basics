# Variabel Global

g = 10

def f1():
    print('Nilai variabel g didalam f1(): %d' %g)

def f2():
    print('Nilai variabel g didalam f2(): %d' %g)

def main():
    # memnanggil f1 dan f2
    f1()
    f2()

if __name__ == '__main__':
    main()